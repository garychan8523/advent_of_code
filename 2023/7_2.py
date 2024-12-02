lines = open('7_2.in', 'r')

hand_bid_dict = {}
def get_type(cards):
    max_type = -1
    # if J in cards
    if 1 in cards:
        for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
            t = []
            for card in cards:
                if card == 1:
                    t.append(num)
                else:
                    t.append(card)
            t_type = _get_type(t)
            if t_type > max_type:
                max_type = t_type
        return max_type
    else:
        return _get_type(cards)


def _get_type(cards):

    unique_cards = len(set(cards))
    unique_count = set([cards.count(i) for i in cards])

    # print(f'unique_cards {unique_cards} unique_count {unique_count}')

    # type 7 (Five of a kind, AAAAA)
    if unique_cards == 1:
        return 7
    
    # type 6 (Four of a kind, AA8AA)
    if unique_cards == 2 and unique_count == {4, 1}:
        return 6
    
    # type 5 (Full house, 23332)
    if unique_cards == 2 and unique_count == {3, 2}:
        return 5
    
    # type 4 (Three of a kind, TTT98)
    if unique_cards == 3 and unique_count == {3, 1}:
        return 4
    
    # type 3 (Two pair, 23432)
    if unique_cards == 3 and unique_count == {2, 1}:
        return 3
    
    # type 2 (One pair, A23A4)
    if unique_cards == 4 and unique_count == {2, 1}:
        return 2
    
    # type 1 (High card, 23456)
    if unique_cards == 5:
        return 1
    
    return -1


def compare(x, y):
    if x['card_type'] > y['card_type']:
        return 1
    if x['card_type'] < y['card_type']:
        return -1
    
    if x['card_type'] == y['card_type']:
        for i in range(len(x['cards'])):
            if x['cards'][i] > y['cards'][i]:
                return 1
            if x['cards'][i] < y['cards'][i]:
                return -1
    
    return 0

hands = []

for line in lines:
    line = line.strip()
    
    cards = line.split(' ')[0]
    t = []
    for card in cards:
        if card == 'T':
            t.append(10)
        elif card == 'J':
            t.append(1)
        elif card == 'Q':
            t.append(11)
        elif card == 'K':
            t.append(12)
        elif card == 'A':
            t.append(13)
        else:
            t.append(int(card))
    cards = t

    card_type = get_type(cards)

    bid = int(line.split(' ')[1])

    hand = {'cards': cards, 'card_type': card_type, 'bid': bid}
    print(f'hand {hand}')

    hands.append(hand)


from functools import cmp_to_key

hands = sorted(hands, key=cmp_to_key(compare))

print(f'hands {hands}')

g_sum = 0

for i in range(len(hands)):
    #print(f"debug {hands[i]['bid']} * {i+1}")
    hand_sum = hands[i]['bid'] * int(i+1)
    g_sum += hand_sum

print(f'g_sum {g_sum}')

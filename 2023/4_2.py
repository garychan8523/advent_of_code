
card_total = sum(1 for _ in open('4_2.in'))
print(f'card_total {card_total}')

cards = [1 for _ in range(card_total)]

lines = open('4_2.in', 'r')

g_sum = 0

for line in lines:
    line = line.strip()
    print(line)

    card_num = int(line.split(':')[0].replace(' ', '').replace('Card', ''))
    winning_nums = line.split('|')[0].split(' ')
    winning_nums = [int(i) for i in winning_nums if i.isnumeric()]
    holding_nums = line.split('|')[1].split(' ')
    holding_nums = [int(i) for i in holding_nums if i.isnumeric()]
    print(f'card_num {card_num}, winning_nums {winning_nums}, holding_nums {holding_nums}')

    counter = 0
    for num in holding_nums:
        if num in winning_nums:
            counter += 1
    
    for i in range (card_num+1, card_num+counter+1):
        if i < card_total:
            cards[i] += cards[card_num]


print(f'cards {cards}, sum(cards) {sum(cards)}')
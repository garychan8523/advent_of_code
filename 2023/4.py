lines = open('4.in', 'r')

g_sum = 0
for line in lines:
    line = line.strip()
    print(line)
    winning_nums = line.split('|')[0].split(' ')
    winning_nums = [int(i) for i in winning_nums if i.isnumeric()]
    holding_nums = line.split('|')[1].split(' ')
    holding_nums = [int(i) for i in holding_nums if i.isnumeric()]
    print(f'winning_nums {winning_nums}, holding_nums {holding_nums}')

    counter = 0
    for num in holding_nums:
        if num in winning_nums:
            counter += 1
    
    card_sum = pow(2, counter-1) if counter > 0 else 0
    print (f'card_sum {card_sum}')
    g_sum += card_sum


print(f'g_sum {g_sum}')
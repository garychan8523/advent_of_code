lines = open('15.in', 'r')

for line in lines:
    line = line.strip().split(',')

inputs = line

g_sum = 0
for input in inputs:
    l_sum = 0
    if '-' in input:
        operator = '-'
        label = input[:input.find('-')]
    if '=' in input:
        operator = '='
        label = input[:input.find('=')]
        focal_length = input[input.find('=')+1:]
    for char in label:
        l_sum += ord(char)
        l_sum *= 17
        l_sum = l_sum%256
    print(f'l_sum {l_sum}')
    g_sum += l_sum

print(f'g_sum {g_sum}')


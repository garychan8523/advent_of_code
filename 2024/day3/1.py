

import re  


def solver(line):
    
    regex = 'mul[(][0-9]*,[0-9]*[)]'             

    matches = re.findall(regex, line)
    print(matches)

    total = 0
    for match in matches:
        match = match.replace('mul(', '')
        match = match.replace(')', '')
        splited = match.split(',')
        left = int(splited[0])
        right = int(splited[1])
        total += left * right

    print(total)
    return total



total = 0
lines = open('sample')
lines = [line.strip() for line in lines]
for line in lines:
    total += solver(line)
assert total == 161

total = 0
lines = open('input')
lines = [line.strip() for line in lines]
for line in lines:
    total += solver(line)
assert total == 178538786
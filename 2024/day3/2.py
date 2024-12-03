

import re  


enabled = True

def solver(line):
    global enabled
    regex = "(mul[(][0-9]*,[0-9]*[)]|do[(][)]|don't[(][)])"

    matches = re.findall(regex, line)
    print(matches)

    total = 0
    for match in matches:
        if match == 'do()':
            enabled = True
            continue
        if match == "don't()":
            enabled = False
            continue
        if enabled and match.startswith('mul('):
            match = match.replace('mul(', '')
            match = match.replace(')', '')
            splited = match.split(',')
            left = int(splited[0])
            right = int(splited[1])
            total += left * right

    print(total)
    return total



total = 0
lines = open('sample2')
lines = [line.strip() for line in lines]
for line in lines:
    total += solver(line)
assert total == 48

total = 0
lines = open('input')
lines = [line.strip() for line in lines]
for line in lines:
    total += solver(line)
assert total == 102467299

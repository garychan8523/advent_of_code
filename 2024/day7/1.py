

def transform(lines):
    lines = [line.strip() for line in lines]
    lines = [line.split(':') for line in lines]
    for i in range(len(lines)):
        target = int (lines[i][0])
        values = lines[i][1][1:].split(' ')
        values = [int(value) for value in values]
        lines[i] = (target, values)

    return lines


def solver(current, target, remains):
    # print(f'sover {current} {target} {remains}')
    if len(remains) == 0:
        return current == target
    if current > target:
        return False

    operators = ['+', '*']

    for operator in operators:
        new_value = eval(f'{current} {operator} {remains[0]}')
        result = solver(new_value, target, remains[1:])
        if result:  return result

    return False


total = 0
lines = transform(open('sample'))
for line in lines:
    target = line[0]
    values = line[1]
    if solver(0, target, values):
        print(f'{target} {values} {sum(values)} is True')
        total += target
print(total)
assert total == 3749


counter = 0
total = 0
lines = transform(open('input'))
for line in lines:
    target = line[0]
    values = line[1]
    if solver(0, target, values):
        total += target
    counter += 1
    print(counter)
print(total)
assert total == 3351424677624







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
    #print(f'sover {current} {target} {remains}')
    if len(remains) == 0 and current == target:
        return True
    
    if len(remains) == 0 and current != target:
        return False

    operators = ['+', '*', '||']

    for operator in operators:
        if operator == '||':
            new_value = int(f'{current}{remains[0]}')
            result = solver(new_value, target, remains[1:])
            if result:  return result
        else:
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
        #print(f'{target} {values} {sum(values)} is True')
        total += target
assert total == 11387



counter = 0
total = 0
lines = transform(open('input'))
for line in lines:
    target = line[0]
    values = line[1]
    if solver(0, target, values):
        total += target
    counter += 1
    # it runs for few mins :-)
    print(counter)
print(total)
assert total == 204976636995111

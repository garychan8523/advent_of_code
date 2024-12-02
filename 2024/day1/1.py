
def solver(lines):
    left = []
    right = []

    for line in lines:
        splited = line.split(' ')
        pair = [int(i) for i in splited if i != '']
        left.append(pair[0])
        right.append(pair[1])

    left.sort()
    right.sort()

    total_distance = 0
    while left:
        total_distance += abs(left.pop(0) - right.pop(0))
    return total_distance



lines = open('sample', 'r')
lines = [line.strip() for line in lines]
out = solver(lines)
print(out)
assert out == 11

lines = open('input', 'r')
lines = [line.strip() for line in lines]
out = solver(lines)
print(out)
assert out == 1341714

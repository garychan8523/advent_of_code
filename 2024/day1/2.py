
def solver(lines):
    left = []
    right = []

    for line in lines:
        splited = line.split(' ')
        pair = [int(i) for i in splited if i != '']
        left.append(pair[0])
        right.append(pair[1])

    total = 0
    for item in left:
        total += item * right.count(item)
    return total


lines = open('sample', 'r')
lines = [line.strip() for line in lines]
out = solver(lines)
print(out)
assert out == 31

lines = open('input', 'r')
lines = [line.strip() for line in lines]
out = solver(lines)
print(out)
assert out == 27384707

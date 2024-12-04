
def solver(lines, target='XMAS'):
    rows = len(lines)
    cols = len(lines[0])
    n = len(target)

    horizontal = 0
    vertical = 0
    diagonal = 0
    for i in range(rows):
        for j in range(cols):
            if j+n <= cols:
                # print(lines[i][j:j+n])
                if lines[i][j:j+n] in (target, target[::-1]):
                    horizontal += 1
            if i+n <= rows:
                # print(''.join([lines[k][j] for k in range(i, i+n)]))
                if ''.join([lines[k][j] for k in range(i, i+n)]) in (target, target[::-1]):
                    vertical += 1
            # /
            if j >= len(target)-1 and i+n <= rows:
                # print([lines[i+k][j-k] for k in range(n)])
                if ''.join([lines[i+k][j-k] for k in range(n)]) in (target, target[::-1]):
                    diagonal += 1
            # \
            if j+n <= cols and i+n <= rows:
                # print([lines[i+k][j+k] for k in range(n)])
                if ''.join([lines[i+k][j+k] for k in range(n)]) in (target, target[::-1]):
                    diagonal += 1

        # print()

    return horizontal + vertical + diagonal


lines = open('sample')
lines = [line.strip() for line in lines]
total = solver(lines)
print(total)
assert total == 18

lines = open('input')
lines = [line.strip() for line in lines]
total = solver(lines)
print(total)
assert total == 2551

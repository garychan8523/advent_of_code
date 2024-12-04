
def solver(line, target='MAS'):
    rows = len(lines)
    cols = len(lines[0])
    n = len(target)

    diagonal = 0
    for i in range(rows):
        for j in range(cols):
            # \
            if j+n <= cols and i+n <= rows:
                print([lines[i+k][j+k] for k in range(n)])
                if ''.join([lines[i+k][j+k] for k in range(n)]) in (target, target[::-1]):
                    # /
                    z = j + 2
                    print([lines[i+k][j-k] for k in range(n)])
                    if ''.join([lines[i+k][z-k] for k in range(n)]) in (target, target[::-1]):
                        diagonal += 1

        print()

    return diagonal


lines = open('sample')
lines = [line.strip() for line in lines]
total = solver(lines)
print(total)

lines = open('input')
lines = [line.strip() for line in lines]
total = solver(lines)
print(total)

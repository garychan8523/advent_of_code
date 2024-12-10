

def display(grid):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            print(grid[i][j], end='')
        print()


def transform(lines):
    lines  = [line.strip() for line in lines]
    lines  = [list(line) for line in lines]
    rows, cols = len(lines), len(lines[0])
    for i in range(rows):
        for j in range(cols):
            try:
                lines[i][j] = int(lines[i][j])
            except:
                pass
    return lines


def get_starts(grid):
    out = []
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                out.append((i, j))
    return out


def is_inbound(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    return row >= 0 and row < rows and col >= 0 and col < cols


def traverse(grid, row, col, visited):
    # print(f'check ({row}, {col}) {grid[row][col]}')
    if (row, col) in visited:
        return 0
    visited.add((row, col))

    if grid[row][col] == 9:
        return 1
    
    out = 0

    trials = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    for trial in trials:
        n_row, n_col = trial[0], trial[1]
        if is_inbound(grid, n_row, n_col) and type(grid[n_row][n_col]) == int and grid[n_row][n_col]-grid[row][col] == 1:
            print(f'at ({row}, {col}) visited {visited}')
            out += traverse(grid, n_row, n_col, visited)

    return out


def solver(grid):
    display(grid)

    starts = get_starts(grid)

    total = 0

    for start in starts:
        start_row, start_col = start[0], start[1]
        print(f'start {start}')
        score = traverse(grid, start_row, start_col, set())
        print(f'score: {score}')
        total += score

    return total



lines = transform(open('sample1_1'))
out = solver(lines)
print(out)
assert out == 2


lines = transform(open('sample1_2'))
out = solver(lines)
print(out)
assert out == 4


lines = transform(open('sample'))
out = solver(lines)
print(out)
assert out == 36


lines = transform(open('input'))
out = solver(lines)
print(out)
assert out == 548

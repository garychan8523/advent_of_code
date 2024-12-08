

def display_grid(grid, positions=None):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if positions and (i, j) in positions:
                print('X', end='')
                continue
            print(grid[i][j], end='')
        print()
    print()


def transform(lines):
    lines = [line.strip() for line in lines]
    lines = [list(line) for line in lines]
    return lines


def is_inbound(grid, position):
    row, col = position[0], position[1]
    rows, cols = len(grid), len(grid[0])
    return row >= 0 and row < rows and col >= 0 and col < cols


def get_direction(positionA, positionB):
    a_row, a_col = positionA[0], positionA[1]
    b_row, b_col = positionB[0], positionB[1]

    if a_row == b_row:
        if b_col <= a_col:
            return 'left'
        else:
            return 'right'
    if a_col == b_col:
        if b_row <= a_row:
            return 'up'
        else:
            return 'down'
    
    if b_row <= a_row:
        if b_col <= a_col:
            return 'top-left'
        else:
            return 'top-right'
    else:
        if b_col <= a_col:
            return 'bottom-left'
        else:
            return 'bottom-right'

def get_extended_position(positionA, positionB, direction):
    a_row, a_col = positionA[0], positionA[1]
    b_row, b_col = positionB[0], positionB[1]

    if direction == 'up':
        new_row = b_row - (a_row - b_row)
        return (new_row, a_col)
    if direction == 'down':
        new_row = b_row + (b_row - a_row)
        return (new_row, a_col)
    if direction == 'left':
        new_col = b_col - (a_col - b_col)
        return (a_row, new_col)
    if direction == 'right':
        new_col = b_col + (b_col - a_col)
        return (a_row, new_col)
    if direction == 'top-left':
        row_diff = a_row-b_row
        col_diff = a_col-b_col
        return (b_row-row_diff, b_col-col_diff)
    if direction == 'top-right':
        row_diff = a_row-b_row
        col_diff = b_col-a_col
        return (b_row-row_diff, b_col+col_diff)
    if direction == 'bottom-left':
        row_diff = b_row-a_row
        col_diff = a_col-b_col
        return (b_row+row_diff, b_col-col_diff)
    if direction == 'bottom-right':
        row_diff = b_row-a_row
        col_diff = b_col-a_col
        return (b_row+row_diff, b_col+col_diff)
    
    
def mark_antinodes(antinodes, positionA, positionB):
    def mark(positionA, positionB):
        while True:
            direction = get_direction(positionA, positionB)
            extended_position = get_extended_position(positionA, positionB, direction)

            if is_inbound(antinodes, extended_position):
                m_row, m_col = extended_position[0], extended_position[1]
                antinodes[m_row][m_col] = '#'

                positionA = (positionB[0], positionB[1])
                positionB = (m_row, m_col)
                extended_position = get_extended_position(positionA, positionB, direction)
            else:
                break
    
    mark(positionA, positionB)
    mark(positionB, positionA)


def solver(grid):
    print('input')
    display_grid(grid)

    signals = {}
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '.':
                signal = grid[i][j]
                if signal not in signals:
                    signals[signal] = [(i, j)]
                else:
                    signals[signal].append((i, j))
    
    print(f'parsed signals {signals}')

    print('antinodes')
    antinodes = [[grid[i][j] for j in range(cols)] for i in range(rows)]
    display_grid(antinodes)

    for signal in signals:
        print(f'\n> signal {signal}')
        positions = signals[signal]
        for i in range(len(positions)):
            current = positions[i]
            remains = positions[i+1:]
            print(f'check {current} with {remains}')

            for remain in remains:
                print(f'    check {current} with {remain}')
                mark_antinodes(antinodes, current, remain)

    print('antinodes after')
    display_grid(antinodes)

    total = 0
    a_row, a_col = len(antinodes), len(antinodes[0])
    for i in range(a_row):
        for j in range(a_col):
            if antinodes[i][j] != '.':
                total += 1
    
    return total



lines = transform(open('sample2'))
out = solver(lines)
print(out)
assert out == 9

lines = transform(open('sample'))
out = solver(lines)
print(out)
assert out == 34

lines = transform(open('input'))
out = solver(lines)
print(out)
assert out == 1280

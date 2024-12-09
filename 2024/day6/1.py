
start_symbols = {'^': 'up', '>': 'right', 'v': 'down', '<': 'left'}
directions = ['up', 'right', 'down', 'left']

def transform(lines):
    lines = [line.strip() for line in lines]
    return [list(line) for line in lines]


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


def get_start(grid):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in start_symbols:
                return ((i, j), start_symbols[grid[i][j]])


def is_inbound(grid, position):
    row, col = position[0], position[1]
    rows, cols = len(grid), len(grid[0])
    return row >= 0 and row < rows and col >= 0 and col < cols


def movable(grid, position):
    row, col = position[0], position[1]
    return grid[row][col] not in ('#')


def get_position(position, direction):
    row, col = position[0], position[1]
    if direction == 'up':   return (row-1, col)
    if direction == 'down':   return (row+1, col)
    if direction == 'left':   return (row, col-1)
    if direction == 'right':   return (row, col+1)
    return None


def rotate_right(direction):
    return directions[(directions.index(direction)+1) % len(directions)]


def solver(grid):
    display_grid(grid)

    start = get_start(grid)
    
    # visited set: {((position), direction), ...}
    visited = set()
    # positions set: {(positon), ...}
    positions = set()
    current = start


    while is_inbound(grid, current[0]):
        if current in visited:
            break
        else:
            visited.add(current)


        position = current[0]
        direction = current[1]
        positions.add(position)

        print(f'{current} at step {len(positions)}')

        if is_inbound(grid, get_position(position, direction)):
            if movable(grid, get_position(position, direction)):
                current = (get_position(position, direction), direction)
            else:
                rotated_position = get_position(position, rotate_right(direction))
                if is_inbound(grid, rotated_position) and movable(grid, rotated_position):
                    current = (get_position(position, rotate_right(direction)), rotate_right(direction))
                else:
                    break
        else:
            break
    
    print()
    print(f'start {start}')
    print()
    display_grid(grid, positions)

    return len(positions)



grid = transform(open('sample'))
total = solver(grid)
print(total)
assert total == 41


grid = transform(open('sample1_1'))
total = solver(grid)
print(total)
assert total == 1


grid = transform(open('sample1_2'))
total = solver(grid)
print(total)
assert total == 2


grid = transform(open('input'))
total = solver(grid)
print(total)
assert total == 5331


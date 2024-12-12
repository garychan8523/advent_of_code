import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')



start_symbols = {"^": "up", ">": "right", "v": "down", "<": "left"}
directions = ['up', 'right', 'down', 'left']

def transform(lines):
    lines = [line.strip() for line in lines]
    return [list(line) for line in lines]


def display_grid(grid, positions=None):
    if logger.level > logging.DEBUG:
        return
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if positions and (i, j) in positions:
                print('X', end='')
                continue
            print(grid[i][j], end='')
        print('')
    print('')


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
    return grid[row][col] not in ("#")


def get_position(position, direction):
    row, col = position[0], position[1]
    if direction == "up":
        return (row - 1, col)
    if direction == "down":
        return (row + 1, col)
    if direction == "left":
        return (row, col - 1)
    if direction == "right":
        return (row, col + 1)
    return None


def rotate_right(direction):
    return directions[(directions.index(direction)+1) % len(directions)]


def solver(grid):
    # display_grid(grid)

    start = get_start(grid)

    # visited set: {((position), direction), ...}
    visited = set()
    # positions set: {(positon), ...}
    positions = set()
    current = start

    while is_inbound(grid, current[0]):
        if current in visited:
            return True
        visited.add(current)

        position = current[0]
        direction = current[1]

        logger.debug(f'{current} at step {len(positions)}')

        position_next = get_position(position, direction)
        if is_inbound(grid, position_next):
            if movable(grid, position_next):
                current = (position_next, direction)
                continue
            else:
                tried = set()
                tried.add((position_next, direction))

                _direction = direction

                while len(tried) < 4:
                    direction_rotated = rotate_right(_direction)
                    position_rotated = get_position(position, direction_rotated)

                    tried.add((position_rotated, direction_rotated))

                    if not is_inbound(grid, position_rotated):
                        # outbound
                        return False

                    if movable(grid, position_rotated):
                        # movable, advancing
                        current = (position_rotated, direction_rotated)
                        break
                    else:
                       # not movable, continue rotation
                       _direction = direction_rotated
               
                if len(tried) == 4:
                    # tried all 4 directions
                    return False
        else:
            break

    return False




grid = transform(open("sample2_1"))
assert solver(grid) is True

grid = transform(open("sample2_2"))
assert solver(grid) is True

grid = transform(open("sample2_3"))
assert solver(grid) is True

grid = transform(open("sample2_4"))
assert solver(grid) is True

grid = transform(open("sample2_5"))
assert solver(grid) is True

grid = transform(open("sample2_6"))
assert solver(grid) is True

grid = transform(open("sample2_7"))
assert solver(grid) is False



total = 0
grid = transform(open("sample"))
rows, cols = len(grid), len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == ".":
            grid_copy = [x[:] for x in grid]
            grid_copy[i][j] = "#"
            if solver(grid_copy):
                display_grid(grid_copy)
                total += 1
print(total)
assert total == 6



logger.setLevel(logging.INFO)
total = 0
grid = transform(open("input"))
rows, cols = len(grid), len(grid[0])

for i in range(rows):
    for j in range(cols):
        if (i * cols + j) % 100 == 0:
            print(f'{i * cols + j} / {rows*cols}')
        if grid[i][j] == ".":
            grid_copy = [x[:] for x in grid]
            grid_copy[i][j] = "#"
            if solver(grid_copy):
                total += 1
print(total)
assert total == 1812

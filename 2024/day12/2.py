import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')



def transform(lines):
    lines = [line.strip() for line in lines]
    lines = [list(line) for line in lines]
    return lines

def display_grid(grid):
    if logger.level > logging.DEBUG:
        return
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            print(grid[i][j], end='')
        print()
    print()

def copy_grid(grid):
    return [x[:] for x in grid]
    
def inbound(grid, position):
    row, col = position[0], position[1]
    rows, cols = len(grid), len(grid[0])
    return row >= 0 and row < rows and col >= 0 and col < cols

def get_value(grid, position):
    row, col = position[0], position[1]
    return grid[row][col]

def expand(grid):
    rows, cols = len(grid), len(grid[0])
    return [['.'] * (cols*2+1) for _ in range(rows*2+1)]

def fill_fence(grid, target):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        if i % 2 == 0:
            continue
        for j in range(cols):
            if j % 2 == 0:
                continue
            if grid[i][j] != target:
                continue

            checks = [(i-2, j), (i+2, j), (i, j-2), (i, j+2)]
            fills = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for k, check in enumerate(checks):
                fill = fills[k]
                if not inbound(grid, check):
                    grid[fill[0]][fill[1]] = '#'
                else:
                    logger.debug(f'check {check} fill {fill}')
                    if get_value(grid, check) != target:
                        grid[fill[0]][fill[1]] = '#'
    return grid

def fill_plant(grid, positions):
    for i, j in positions:
        grid[i][j] = 'O'
    return grid

def connectable(grid, position, target, visited=set()):
    row, col = position[0], position[1]
    if (row, col) in visited:
        return []
    visited.add((row, col))
    if not inbound(grid, position):
        return []
    if grid[row][col] != target:
        return []

    current = []
    current.append((row, col))
    directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    for direction in directions:
        current.extend(connectable(grid, direction, target, visited))
    return current

def to_expanded_position(position):
    row, col = position[0], position[1]
    return (row*2+1, col*2+1)


# for clarity ..
# need to check for a side, there's an plant next to it and all in same facing side
# otherwise for situation like below, (2, 3) and (4, 3) will be incorrectly identified as same side
#  .#.#.#.#.#.
#  #O.O.O.O.O#
#  ...#...#...
#  #O#.#O#.#O#
#  ...#...#...
#  #O.O.O.O.O#
#  .#.#.#.#.#.

def above_inbound_and_is_plant(grid, row, col):
    return inbound(grid, (row-1, col)) and grid[row-1][col] == 'O'

def below_inbound_and_is_plant(grid, row, col):
    return inbound(grid, (row+1, col)) and grid[row+1][col] == 'O'

def left_inbound_and_is_plant(grid, row, col):
    return inbound(grid, (row, col-1)) and grid[row][col-1] == 'O'

def right_inbound_and_is_plant(grid, row, col):
    return inbound(grid, (row, col+1)) and grid[row][col+1] == 'O'


def get_sides(grid):
    rows, cols = len(grid), len(grid[1])

    side = 0

    for i in range(rows):
        for j in range(cols):
            row, col = i, j

            if grid[i][j] != '#':
                continue

            # horizontal
            if j + 2 < cols and grid[i][j+1] == '.' and grid[i][j+2] == '#':

                if below_inbound_and_is_plant(grid, i, j) and below_inbound_and_is_plant(grid, i, j+2):
                    logger.debug(f'{i}, {j}  horizontal with below')
                    grid[i][j] = '.'
                    side += 1
                    while col < cols:
                        if col+2 < cols and grid[row][col+1] == '.' and grid[row][col+2] == '#' and below_inbound_and_is_plant(grid, row, col+2):
                            grid[row][col+2] = '.'
                            col += 2
                        else:
                            break
                    continue

                if above_inbound_and_is_plant(grid, i, j) and above_inbound_and_is_plant(grid, i, j+2):
                    logger.debug(f'{i}, {j}  horizontal with above')
                    grid[i][j] = '.'
                    side += 1
                    while col < cols:
                        if col+2 < cols and grid[row][col+1] == '.' and grid[row][col+2] == '#' and above_inbound_and_is_plant(grid, row, col+2):
                            grid[row][col+2] = '.'
                            col += 2
                        else:
                            break
                    continue
                    
            # vertical
            if i + 2 < rows and grid[i+1][j] == '.' and grid[i+2][j] == '#':

                if left_inbound_and_is_plant(grid, i, j) and left_inbound_and_is_plant(grid, i+2, j):
                    logger.debug(f'{i}, {j}  vertical with left')
                    grid[i][j] = '.'
                    side += 1
                    while row < rows:
                        if row+2 < rows and grid[row+1][col] == '.' and grid[row+2][col] == '#' and left_inbound_and_is_plant(grid, row+2, col):
                            grid[row+2][col] = '.'
                            row += 2
                        else:
                            break
                    continue

                if right_inbound_and_is_plant(grid, i, j) and right_inbound_and_is_plant(grid, i+2, j):
                    logger.debug(f'{i}, {j}  vertical with left')
                    grid[i][j] = '.'
                    side += 1
                    while row < rows:
                        if row+2 < rows and grid[row+1][col] == '.' and grid[row+2][col] == '#' and right_inbound_and_is_plant(grid, row+2, col):
                            grid[row+2][col] = '.'
                            row += 2
                        else:
                            break
                    continue
                        
            # lone cell
            logger.debug(f'{i}, {j}  else')
            side += 1
            grid[i][j] = '.'
    
    logger.debug('after get_sides')
    display_grid(grid)
    
    logger.debug(f'side {side}')
    return side
                

def solver(grid):
    rows, cols = len(grid), len(grid[0])
    display_grid(grid)

    groups = []
    remains = {(i, j) for i in range(rows) for j in range(cols)}
    while remains:
        first = remains.pop()
        connectables = connectable(grid, first, grid[first[0]][first[1]], set())
        groups.append(connectables)
        for item in connectables:
            try:
                remains.remove(item)
            except:
                pass

    for i, group in enumerate(groups):
        for j, position in enumerate(group):
            group[j] = to_expanded_position(position)

    total = 0

    expanded = expand(grid)
    for group in groups:
        count = len(group)

        copy = copy_grid(expanded)

        row, col = group[0]
        logger.debug(f'for {grid[row//2][col//2]},')

        filled = fill_plant(copy, group)
        display_grid(copy)

        filled = fill_fence(filled, target='O')
        logger.debug(f'after fill_fence')
        display_grid(filled)

        sides = get_sides(filled)
        logger.debug(f"count {count} * sides {sides}")
        total += count * sides

    return total

def get_plants_set(grid):
    out = set()
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            out.add(grid[i][j])
    return out


grid = transform(open('sample'))
out = solver(grid)
print(out)
assert out == 80

grid = transform(open('sample1_1'))
out = solver(grid)
print(out)
assert out == 436

grid = transform(open('sample2_1'))
out = solver(grid)
print(out)
assert out == 236

grid = transform(open('sample2_2'))
out = solver(grid)
print(out)
assert out == 368

grid = transform(open('sample2_3'))
out = solver(grid)
print(out)
assert out == 1206

logger.setLevel(logging.INFO)
grid = transform(open('input'))
out = solver(grid)
print(out)
assert out == 814302

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
                    grid[fill[0]][fill[1]] = 'X'
                else:
                    logger.debug(f'check {check} fill {fill}')
                    if get_value(grid, check) != target:
                        grid[fill[0]][fill[1]] = 'X'

    return grid
            
def fill_plant(grid, positions):
    rows, cols = len(grid), len(grid[0])
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
    
    logger.debug(f'groups: {groups}')

    for i, group in enumerate(groups):
        for j, position in enumerate(group):
            group[j] = to_expanded_position(position)

    logger.debug(f'groups: {groups}')

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
        display_grid(filled)

        logger.debug(f"count {count} * {sum(row.count('X') for row in filled)}")
        total += count * sum(row.count('X') for row in filled)

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
assert out == 140


grid = transform(open('sample1_1'))
out = solver(grid)
print(out)
assert out == 772


grid = transform(open('sample1_2'))
out = solver(grid)
print(out)
assert out == 1930


logger.setLevel(logging.INFO)
grid = transform(open('input'))
out = solver(grid)
print(out)
assert out == 1344578

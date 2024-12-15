
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')



def display_grid(grid):
    if logger.level > logging.DEBUG:
        return
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            print(grid[i][j], end='')
        print()
    print()


def get_target(grid, target):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == target:
                return (i, j)
    return False


def get_position_value(grid, position):
    row, col = position[0], position[1]
    return grid[row][col]


def get_gps(grid):
    rows, cols = len(grid), len(grid[0])
    out = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                out += i * 100 + j
    return out


def transform(lines):
    lines = [line.strip() for line in lines]

    grid = []
    moves = []

    is_grid = True
    for line in lines:
        if len(line) == 0:
            is_grid = False
            continue
        
        if is_grid:
            grid.append(list(line))
        else:
            for char in line:
                if char == '^':
                    moves.append(0)
                if char == '>':
                    moves.append(1)
                if char == 'v':
                    moves.append(2)
                if char == '<':
                    moves.append(3)
    return (grid, moves)


def solver(grid, moves):
    rows, cols = len(grid), len(grid[0])

    start = get_target(grid, '@')
    display_grid(grid)
    logger.debug(f'moves {moves}')
    logger.debug(f'start {start}')

    current = start
    for move in moves:
        logger.debug(f'at {current} attempt move {move}')

        row, col = current[0], current[1]

        directions = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]

        new_position = directions[move]
        n_row, n_col = new_position
        logger.debug(f'new position {new_position}')

        new_position_object = get_position_value(grid, new_position)
        logger.debug(f'new_position_object {new_position_object}')

        # wall
        if new_position_object == '#':
            logger.debug('no move')

        if new_position_object == '.':
            logger.debug('is road, move')
            grid[row][col] = '.'
            grid[n_row][n_col] = '@'
            current = new_position
        
        # 0: up, 1: right, 2: down, 3: left
        if new_position_object == 'O':
            # right
            if move == 1:
                rest = []
                for j in range(col+1, cols):
                    if grid[row][j] == '#':
                        break
                    rest.append(grid[row][j])
                logger.debug(f'rest {rest}')

                if '.' not in rest:
                    logger.debug('not pushable')
                    continue

                for x in range(col+1, cols):
                    if grid[row][x] == '.':
                        break
                
                grid[row][x] = 'O'
                grid[row][col] = '.'
                grid[n_row][n_col] = '@'
                current = new_position
            
            # left
            if move == 3:
                rest = []
                for j in range(col-1, -1, -1):
                    if grid[row][j] == '#':
                        break
                    rest.append(grid[row][j])
                logger.debug(f'rest {rest}')

                if '.' not in rest:
                    logger.debug('not pushable')
                    continue

                for x in range(col-1, -1, -1):
                    if grid[row][x] == '.':
                        break
                
                grid[row][x] = 'O'
                grid[row][col] = '.'
                grid[n_row][n_col] = '@'
                current = new_position

            # down
            if move == 2:
                rest = []
                for i in range(row+1, rows):
                    if grid[i][col] == '#':
                        break
                    rest.append(grid[i][col])
                logger.debug(f'rest {rest}')

                if '.' not in rest:
                    logger.debug('not pushable')
                    continue
                
                for x in range(row+1, rows):
                    if grid[x][col] == '.':
                        break
                
                grid[x][col] = 'O'
                grid[row][col] = '.'
                grid[n_row][n_col] = '@'
                current = new_position
            
            # up
            if move == 0:
                rest = []
                for i in range(row-1, -1, -1):
                    if grid[i][col] == '#':
                        break
                    rest.append(grid[i][col])
                logger.debug(f'rest {rest}')

                if '.' not in rest:
                    logger.debug('not pushable')
                    continue
                
                for x in range(row-1, -1, -1):
                    if grid[x][col] == '.':
                        break
                
                grid[x][col] = 'O'
                grid[row][col] = '.'
                grid[n_row][n_col] = '@'
                current = new_position
            

        display_grid(grid)

    gps = get_gps(grid)
    logger.debug(f'gps {gps}')

    return gps




grid, moves = transform(open('sample1_1'))
out = solver(grid, moves)
print(out)
assert out == 2028


logger.setLevel(logging.INFO)

grid, moves = transform(open('sample'))
out = solver(grid, moves)
print(out)
assert out == 10092


grid, moves = transform(open('input'))
out = solver(grid, moves)
print(out)
assert out == 1465523

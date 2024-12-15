
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
            if grid[i][j] == '[':
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
    
    rows, cols = len(grid), len(grid[0])
    expanded = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if grid[i][j] == '#':
                row.append('#')
                row.append('#')
            if grid[i][j] == 'O':
                row.append('[')
                row.append(']')
            if grid[i][j] == '.':
                row.append('.')
                row.append('.')
            if grid[i][j] == '@':
                row.append('@')
                row.append('.')
        expanded.append(row)

    return (expanded, moves)


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
        if new_position_object in ('[', ']'):
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
                
                open = False
                for j in range(x, col, -1):
                    if open:
                        grid[row][j] = '['
                    else:
                        grid[row][j] = ']'
                    open = not open
                
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
                
                open = True
                for j in range(x, col):
                    if open:
                        grid[row][j] = '['
                    else:
                        grid[row][j] = ']'
                    open = not open
                
                grid[row][col] = '.'
                grid[n_row][n_col] = '@'
                current = new_position

            # down
            if move == 2:
                move_down_result = move_down(grid, row=row, start=col, end=col)
                if move_down_result:
                    logger.debug(f'move_down_result {move_down_result}')
                    current = move_down_result
                else:
                    logger.debug('cant move down')
            
            # up
            if move == 0:
                move_up_result = move_up(grid, row=row, start=col, end=col)
                if move_up_result:
                    logger.debug(f'move_up_result {move_up_result}')
                    current = move_up_result
                else:
                    logger.debug('cant move up')

        display_grid(grid)

    gps = get_gps(grid)
    logger.debug(f'gps {gps}')

    return gps


def move_up(grid, row, start, end):
    logger.debug(f'move_up: row {row} start {start} end {end}')

    if row-1 <= 0:
        return False
    
    above_start, above_end = start, end
    above = grid[row-1][above_start:above_end+1]
    logger.debug(f'row {row} range is {grid[row][start:end+1]}')
    logger.debug(f'above same range is {above_start} {above_end} {above}')

    if len(above) == above.count('.'):
        logger.debug(f'row {row} {start} {end} can move_up')
        logger.debug('above all pushable, return True')
        for i in range(start, end+1):
            grid[row-1][i] = grid[row][i]
            grid[row][i] = '.'
        return True

    if above.count('#') > 0:
        logger.debug(f'above # > 0, cant move up')
        return False

    # expand range if needed
    if above[0] == ']':
        above_start -= 1
    if above[-1] == '[':
        above_end += 1
    above = grid[row-1][above_start:above_end+1]
    logger.debug(f'row {row} above expanded range is {above_start} {above_end} {above}')

    above_range_start, above_range_end = None, None
    for i in range(above_start, above_end+1):
        if grid[row-1][i] == '[':
            above_range_start = i
            break
    for i in range(above_end, above_start-1, -1):
        if grid[row-1][i] == ']':
            above_range_end = i
            break
    
    logger.debug(f'row {row} above_range_start {above_range_start} above_range_end {above_range_end}')

    if move_up(grid, row-1, above_range_start, above_range_end):
        logger.debug(f'row {row} {start} {end} can move_up')
        logger.debug(f'above_start {above_start} above_end {above_end+1}')
        for i in range(start, end+1):
            if grid[row][i] in ('[', ']', '@'):
                if grid[row][i] == '@':
                    grid[row-1][i] = '@'
                    grid[row][i] = '.'
                    return (row-1, i)
                grid[row-1][i] = grid[row][i]
                grid[row][i] = '.'
            else:
                grid[row-1][i] = '.'
        return True
    else:
        return False


def move_down(grid, row, start, end):
    rows = len(grid)
    logger.debug(f'move_down: row {row} start {start} end {end}')

    if row+1 >= rows-1:
        return False
    
    below_start, below_end = start, end
    below = grid[row+1][below_start:below_end+1]
    logger.debug(f'row {row} range is {grid[row][start:end+1]}')
    logger.debug(f'below same range is {below_start} {below_end} {below}')

    if len(below) == below.count('.'):
        logger.debug(f'row {row} {start} {end} can move_down')
        logger.debug('below all pushable, return True')
        for i in range(start, end+1):
            grid[row+1][i] = grid[row][i]
            grid[row][i] = '.'
        return True
    
    if below.count('#') > 0:
        logger.debug(f'below # > 0, cant move down')
        return False

    # expand range if needed
    if below[0] == ']':
        below_start -= 1
    if below[-1] == '[':
        below_end += 1
    below = grid[row+1][below_start:below_end+1]
    logger.debug(f'row {row} below expanded range is {below_start} {below_end} {below}')

    below_range_start, below_range_end = None, None
    for i in range(below_start, below_end+1):
        if grid[row+1][i] == '[':
            below_range_start = i
            break
    for i in range(below_end, below_start-1, -1):
        if grid[row+1][i] == ']':
            below_range_end = i
            break
    
    logger.debug(f'row {row} below_range_start {below_range_start} below_range_end {below_range_end}')

    if move_down(grid, row+1, below_range_start, below_range_end):
        logger.debug(f'row {row} {start} {end} can move_down')
        logger.debug(f'below_start {below_start} below_end {below_end+1}')
        for i in range(start, end+1):
            if grid[row][i] in ('[', ']', '@'):
                if grid[row][i] == '@':
                    grid[row+1][i] = '@'
                    grid[row][i] = '.'
                    return (row+1, i)
                grid[row+1][i] = grid[row][i]
                grid[row][i] = '.'
            else:
                grid[row+1][i] = '.'
        return True
    else:
        logger.debug(f'row {row} returning False')
        return False




logger.setLevel(logging.INFO)

grid, moves = transform(open('sample'))
out = solver(grid, moves)
print(out)
assert out == 9021


grid, moves = transform(open('input'))
out = solver(grid, moves)
print(out)
assert out == 1471049

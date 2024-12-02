lines = open('3.in', 'r')

matrix = []
for line in lines:
    matrix.append(line.strip())

MATRIX_ROWS = len(matrix)
MATRIX_COLS = len(matrix[0])

def is_valid(row, line_group):
    for col in range(line_group['start'], line_group['end']+1):
        if symbol_connectable(row, col):
            return True
    return False

def symbol_connectable(row, col):
    connectable = False
    # upper row
    if row-1 >= 0:
        # upper left
        if col-1 >= 0:
            if is_symbol(matrix[row-1][col-1]):
                connectable = True
        # upper middle
        if is_symbol(matrix[row-1][col]):
                connectable = True
        # upper right
        if col+1 < MATRIX_COLS:
            if is_symbol(matrix[row-1][col+1]):
                connectable = True
    
    # lower row
    if row+1 < MATRIX_ROWS:
        # lower left
        if col-1 >= 0:
            if is_symbol(matrix[row+1][col-1]):
                connectable = True
        # lower middle
        if is_symbol(matrix[row+1][col]):
            connectable = True
        # lower right
        if col+1 < MATRIX_COLS:
            if is_symbol(matrix[row+1][col+1]):
                connectable = True
    
    # left
    if col-1 >= 0:
        if is_symbol(matrix[row][col-1]):
            connectable = True

    # right
    if col+1 < MATRIX_COLS:
        if is_symbol(matrix[row][col+1]):
            connectable = True
    
    return connectable


def is_symbol(char):
    return not char.isnumeric() and char != '.'

valid_nums = []

row = 0
for line in matrix:
    line = line.strip()
    print(f'row {row}')

    line_groups = []

    t, start, end = '', -1, -1
    for i in range(len(line)):
        if line[i].isnumeric():
            t += line[i]
            if start == -1:
                start = i
            if (i+1 < len(line) and not line[i+1].isnumeric()) or i+1 == len(line):
                end = i
                line_groups.append({'num': int(t), 'start': start, 'end': end})
                t, start, end = '', -1, -1
    print(f'line_groups {line_groups}')
    
    for line_group in line_groups:
        if is_valid(row, line_group):
            valid_nums.append(line_group['num'])
    row += 1


print(f'valid_nums {valid_nums}, sum(valid_nums) {sum(valid_nums)}')


        



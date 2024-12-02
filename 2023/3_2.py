lines = open('3_2.in', 'r')

matrix = []
for line in lines:
    matrix.append(line.strip())

MATRIX_ROWS = len(matrix)
MATRIX_COLS = len(matrix[0])

gear_connectting_nums = {}

def is_valid(row, line_group):
    for col in range(line_group['start'], line_group['end']+1):
        if symbol_connectable(row, col, line_group['num']):
            return True
    return False

def update_gear_connectting_nums(position, num):
    if position in gear_connectting_nums:
        gear_connectting_nums[position].append(num)
    else:
        gear_connectting_nums[position] = [num]

def symbol_connectable(row, col, num):
    connectable = False
    # upper row
    if row-1 >= 0:
        # upper left
        if col-1 >= 0:
            if is_gear(matrix[row-1][col-1]):
                connectable = True
                update_gear_connectting_nums((row-1, col-1), num)
        # upper middle
        if is_gear(matrix[row-1][col]):
                connectable = True
                update_gear_connectting_nums((row-1, col), num)
        # upper right
        if col+1 < MATRIX_COLS:
            if is_gear(matrix[row-1][col+1]):
                connectable = True
                update_gear_connectting_nums((row-1, col+1), num)
    
    # lower row
    if row+1 < MATRIX_ROWS:
        # lower left
        if col-1 >= 0:
            if is_gear(matrix[row+1][col-1]):
                connectable = True
                update_gear_connectting_nums((row+1, col-1), num)
        # lower middle
        if is_gear(matrix[row+1][col]):
            connectable = True
            update_gear_connectting_nums((row+1, col), num)
        # lower right
        if col+1 < MATRIX_COLS:
            if is_gear(matrix[row+1][col+1]):
                connectable = True
                update_gear_connectting_nums((row+1, col+1), num)
    
    # left
    if col-1 >= 0:
        if is_gear(matrix[row][col-1]):
            connectable = True
            update_gear_connectting_nums((row, col-1), num)

    # right
    if col+1 < MATRIX_COLS:
        if is_gear(matrix[row][col+1]):
            connectable = True
            update_gear_connectting_nums((row, col+1), num)
    
    return connectable

def is_gear(char):
    return char == '*'


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
        is_valid(row, line_group)
    row += 1


print(f'gear_connectting_nums {gear_connectting_nums}')

out = []
for value in gear_connectting_nums.values():
    if len(value) > 1:
        t_sum = 1
        for item in value:
            t_sum *= item
        out.append(t_sum)

print(f'out {out}')
print(f'sum(out) {sum(out)}')

import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')


def transform(line):
    line = line.split(' ')
    line = [int(item) for item in line]
    return line


def copy_without_index(_list, index):
    return [_list[i] for i in range(len(_list)) if i != index]


def is_safe(line, tolerance):
    logger.debug(f'{line} tolerance: {tolerance}')
    if tolerance < 0:
        return False
    if len(line) <= 1:
        return True
    
    all_increasing_decreasing = False
    increasing = []
    for i in range(1, len(line)):
        if abs(line[i] - line[i-1]) < 1 or abs(line[i] - line[i-1]) > 3:
            remove_last = is_safe(copy_without_index(line, i), tolerance-1)
            remove_second_last = is_safe(copy_without_index(line, i-1), tolerance-1)
            return remove_last or remove_second_last
        
        if line[i] - line[i-1] == 0:
            increasing.append(0)
        if line[i] - line[i-1] > 0:
            increasing.append(True)
        if line[i] - line[i-1] < 0:
            increasing.append(False)
        
        if i >= 2 and increasing[-1] != increasing[-2]:
            remove_last = is_safe(copy_without_index(line, i), tolerance-1)
            remove_second_last = is_safe(copy_without_index(line, i-1), tolerance-1)
            remove_third_last = is_safe(copy_without_index(line, i-2), tolerance-1)
            
            logger.debug(f'remove_last {remove_last}')
            logger.debug(f'remove_second_last {remove_second_last}')
            logger.debug(f'remove_third_last {remove_third_last}')
            return remove_last or remove_second_last or remove_third_last
        
    if increasing.count(True) == len(increasing) or increasing.count(False) == len(increasing):
        all_increasing_decreasing = True

    return all_increasing_decreasing



assert is_safe([80, 82, 81, 82, 83, 85, 88], 1) == True
assert is_safe([48, 51, 54, 55, 58, 57, 55], 1) == False
assert is_safe([58, 56, 58, 59, 60, 62, 63, 65], 1) == True
assert is_safe([60, 58, 62, 65, 66, 69, 71], 1) == True


def solver(lines):
    safe = 0
    tolerance = 1
    for line in lines:
        line = transform(line)
        out = is_safe(line, tolerance)
        if out:
            safe += 1
        
        print(f'{line} {out}')
    return safe


lines = open('sample')
lines = [line.strip() for line in lines]
out = solver(lines)
print(out)
assert out == 4

lines = open('input')
lines = [line.strip() for line in lines]
out = solver(lines)
print(out)
assert out == 271

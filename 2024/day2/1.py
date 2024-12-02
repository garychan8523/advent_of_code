import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')


def transform(line):
    line = line.split(' ')
    line = [int(item) for item in line]
    return line


def is_safe(line, tolerance):
    logger.debug(f'{line}, {tolerance}')
    if len(line) <= 1:
        return True
    
    all_increasing_decreasing = False
    increasing = []
    differ_exceeds_threshold = False
    for i in range(1, len(line)):
        if abs(line[i] - line[i-1]) < 1 or abs(line[i] - line[i-1]) > 3:
            differ_exceeds_threshold = True
        if line[i] - line[i-1] > 0:
            increasing.append(True)
        if line[i] - line[i-1] < 0:
            increasing.append(False)
    
    if increasing.count(True) == len(line)-1 or increasing.count(False) == len(line)-1:
        all_increasing_decreasing = True
    
    logger.debug(f'all_increasing_decreasing {all_increasing_decreasing}')
    logger.debug(f'differ_exceeds_threshold {differ_exceeds_threshold}')

    return all_increasing_decreasing and not differ_exceeds_threshold


def solver(lines):
    safe = 0
    tolerance = 1
    for line in lines:
        line = transform(line)
        if is_safe(line, tolerance):
            safe += 1
    return safe


lines = open('sample')
lines = [line.strip() for line in lines]
out = solver(lines)
print(out)
assert solver(lines) == 2


lines = open('input')
lines = [line.strip() for line in lines]
out = solver(lines)
print(out)
assert out == 202

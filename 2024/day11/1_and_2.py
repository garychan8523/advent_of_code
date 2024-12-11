import math
from functools import lru_cache


def transform(lines):
    lines = [line.strip() for line in lines]
    lines = [line.split(' ') for line in lines]
    lines = [int(item) for line in lines for item in line]
    return lines


@lru_cache
def get_digits_length(num):
    return int(math.log10(num))+1

@lru_cache
def get_first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

@lru_cache
def get_last_n_digits(num, n):
    return abs(num) % (10**n)

@lru_cache(maxsize=274_877_906_944)
def blink(num, target, iter=0):
    # print(f'blink {num} target: {target}  iter: {iter}  count: {count}')
    if iter == target:
        return 1
    
    iter += 1

    if num == 0:
        return blink(1, target, iter)
    
    digits_length = get_digits_length(num)
    if digits_length % 2 == 0:
        half_length = digits_length // 2
        left_count = blink(get_first_n_digits(num, half_length), target, iter)
        right_count = blink(get_last_n_digits(num, half_length), target, iter)
        return left_count + right_count
    else:
        return blink(num * 2024, target, iter)

    
    
def solver(stone, target):
    return blink(stone, target, iter=0)



out = 0
stones = transform(open('sample'))
for stone in stones:
    out += solver(stone, target=1)
print(f'out {out}')
assert out == 7


out = 0
stones = transform(open('sample1_1'))
for stone in stones:
    out += solver(stone, target=6)
print(f'out {out}')
assert out == 22

out = 0
stones = transform(open('sample1_1'))
for stone in stones:
    out += solver(stone, target=25)
print(f'out {out}')
assert out == 55312


out = 0
stones = transform(open('input'))
for stone in stones:
    out += solver(stone, target=25)
print(f'out {out}')
assert out == 217812


out = 0
stones = transform(open('input'))
for i in range(len(stones)):
    print(f'{i} / {len(stones)}')
    out += solver(stones[i], target=75)
print(f'out {out}')

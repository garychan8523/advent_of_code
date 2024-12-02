# input = ['.??..??...?##.', (1,1,3)]
# input = ['?###????????', (3,2,1)]

inputs = []

lines = open('12.in', 'r')

for line in lines:
    line = line.strip()
    text = line.split(' ')[0]
    config = eval('(' + line.split(' ')[1] + ')')
    inputs.append((text, config))


def replace_next(_str, key, replacement):
    return _str[:_str.find(key)] + replacement + _str[_str.find(key)+1:]


def valid(s):
    while '..' in s:
        s = s.replace('..', '.')
    if s[0] == '.':
        s = s[1:]
    if s[-1] == '.':
        s = s[:-1]
    return s == target


g_sum = 0
for input in inputs:
    row = input[0]
    config = input[1]

    target = ''
    for i in config:
        target += '#'*i + '.'
    else:
        target = target[:-1]
    
    print(f'row\n{row}\n')
    print(f'config\n{config}\n')
    #.#.###
    print(f'target\n{target}\n')

    n = row.count('?')
    r = sum(config) - row.count('#')

    pool = ['#']*r + ['.']*(n-r)
    print(f'pool {pool}')

    from itertools import permutations
    _permutations = list(set(permutations(pool)))
    print(f'_permutations {_permutations}')


    ts = []
    counter = 0
    for permutation in _permutations:
        t = row
        for char in permutation:
            t = replace_next(t, '?', char)
        ts.append(t)

    #print(f'ts {ts}')
    valids = [valid(s) for s in ts].count(True)
    print(f'valids {valids}')
    g_sum += valids

print(g_sum)

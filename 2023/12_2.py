from itertools import permutations

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


def valid(s, target):
    print(f'valid({s}, {target})')
    while '..' in s:
        s = s.replace('..', '.')
    if s[0] == '.':
        s = s[1:]
    if s[-1] == '.':
        s = s[:-1]
    if target[0] == '.':
        target = target[1:]
    if target[-1] == '.':
        target = target[:-1]
    return s == target


from functools import lru_cache
@lru_cache(maxsize=1024)
def expansion_combinations(n, k):
    out = []
    for item in __expansion_combinations(n, k):
        out.append(item)
    return out


def __expansion_combinations(n, k):
    if n == 1:
        yield (k,)
    else:
        for x in range(0, k):
            for i in expansion_combinations(n - 1, k - x):
                yield (x,) + i


def replace_by_expansion(row, expansion):
    for i in expansion:
        row = row.replace('.', 'a'*i, 1)
    row = row.replace('a', '.')
    return row

# print(f"replace_by_expansion {replace_by_expansion('.###########.######.', (0, 1, 2))}")


def fits_with_input(row, new):
    for i in range(len(row)):
        if row[i] == '?':
            continue
        if row[i] == '#' and new[i] != '#':
            return False
        if row[i] == '.' and new[i] != '.':
            return False
    return True


g_sum = 0
for input in inputs:
    row = input[0]
    config = input[1]

    target = ''
    for i in config:
        target += '#'*i + '.'
    else:
        target = target[:-1]
    target = '.' + target + '.'
    
    print(f'row\t{row}')
    print(f'target\t{target}')
    print(f'config\t{config}')
    

    targets = []
    if len(target) - len(row) == 1:
        targets.append(target[1:])
        targets.append(target[:-1])
    elif len(target) - len(row) == 2:
        targets.append(target[1:-1])
    else:
        targets.append(target)
    
    print(f'targets {targets}')
    candidates = set()
    for target in targets:
        n = target.count('.')
        k = target.count('#')

        print(f'n {n}, k {len(row)-k}')
        _expansion_combinations = expansion_combinations(n, len(row)-k)
        print(f'_expansion_combinations\n{_expansion_combinations}\n')

        expansion_combinations_set = set()
        for expansion_combination in _expansion_combinations:
            for item in list(permutations(expansion_combination)):
                expansion_combinations_set.add(item)
        _expansion_combinations = list(expansion_combinations_set)
        print(f'_expansion_combinations\n{_expansion_combinations}\n')

        for expansion_combination in expansion_combinations_set:
            print(f'expansion_combination {expansion_combination}')
            t = replace_by_expansion(target, expansion_combination)
            print(f't {t}') 
            if fits_with_input(row, t) and valid(t, target):
                candidates.add(t)
    print(f'candidates\n{candidates}\n')
    g_sum += len(candidates)

print(g_sum)
exit()

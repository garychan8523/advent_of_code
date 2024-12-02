lines = open('15.in', 'r')

for line in lines:
    line = line.strip().split(',')

inputs = line

_dict = {}
for i in range(256):
    _dict[i] = []
print(f'_dict {_dict}')


def _upsert(key, input):
    target_label = input[:input.find('=')]
    update = False
    for i in range(len(_dict[key])):
        label = _dict[key][i][:_dict[key][i].find('=')]
        if label == target_label:
            _dict[key][i] = input
            update = True
    if not update:
        _dict[key].append(input)


def _pop(key, input):
    target_label = input[:input.find('=')]
    t = []
    for item in _dict[key]:
        label = item[:item.find('=')]
        if label != target_label:
            t.append(item)
    _dict[key] = t


for input in inputs:
    hash = 0
    if '-' in input:
        operator = '-'
        label = input[:input.find('-')]
    if '=' in input:
        operator = '='
        label = input[:input.find('=')]
        focal_length = input[input.find('=')+1:]

    for char in label:
        hash += ord(char)
        hash *= 17
        hash = hash%256
    print(f'hash {hash}')

    if operator == '=':
        _upsert(hash, input)
    else:
        _pop(hash, input)



t = {}
for key in _dict.keys():
    if len(_dict[key]) != 0:
        t[key] = _dict[key]
_dict = t
print(f'_dict {_dict}')



# _dict {0: ['rn=1', 'cm=2'], 3: ['ot=7', 'ab=5', 'pc=6']}
g_sum = 0
for key in _dict.keys():
    lens = _dict[key]
    box_value = key+1
    for i in range(len(lens)):
        slot_value = i+1
        focal_length_value = lens[i][lens[i].find('=')+1:]
        l_sum = box_value * slot_value * int(focal_length_value)
        g_sum += l_sum

print(f'g_sum {g_sum}')
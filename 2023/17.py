lines = open('17.in', 'r')

input = []
for line in lines:
    line = line.strip()
    input.append(line)

h, w = len(input), len(input[0])

def display(_map, name=''):
    h, w = len(_map), len(_map[0])
    if len(name) > 0:
        print(name)
    for i in range(h):
        for j in range(w):
            print(_map[i][j], end='')
        print()
    print()


display(input, 'input')

from enum import Enum
class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def get_path():
    pass



import itertools
_permutations = [p for p in itertools.product([Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT], repeat=3)]
t = []
for permutation in _permutations:
    if Direction.UP in permutation and Direction.DOWN in permutation:
        pass
    elif Direction.LEFT in permutation and Direction.RIGHT in permutation:
        pass
    else:
        t.append(permutation)
_permutations = t


print(f'_permutations {_permutations} len(_permutations) {len(_permutations)}')


def get_position(current, direction):
    if type(current) != tuple:
        return False
    row, col = current[0], current[1]
    output = None
    if direction == Direction.UP:
        output = (row-1, col)
    elif direction == Direction.DOWN:
        output = (row+1, col)
    elif direction == Direction.LEFT:
        output = (row, col-1)
    elif direction == Direction.RIGHT:
        output = (row, col+1)
    
    if output[0] >= 0 and output[0] < h and output[1] >= 0 and output[1] < w:
        return output
    else:
        return False


def get_heat_loss(pos):
    row, col = pos[0], pos[1]
    if row >= 0 and row < h and col >= 0 and col < w:
        return int(input[row][col])
    else:
        return None

import sys
def fill_distance(pos: tuple, _dict: dict):
    min_heat_losses = sys.maxsize
    min_heat_losses_instruction = None
    for i, j, k in _dict.keys():
        positions = []
        positions.append(get_position(pos, i))
        positions.append(get_position(positions[0], j))
        positions.append(get_position(positions[1], k))
        print(f'positions {positions}')
        if not all(positions):
            continue
        heat_losses = [get_heat_loss(pos) for pos in positions]
        heat_losses = sum(heat_losses)
        memory[(i, j, k)] = heat_losses
        if heat_losses < min_heat_losses:
            min_heat_losses = heat_losses
            min_heat_losses_instruction = (i, j, k)
            min_heat_losses_positions = positions


    print(f'min heat loss {min_heat_losses}, min_heat_losses_instruction {min_heat_losses_instruction}, min_heat_losses_positions {min_heat_losses_positions}')


        


pos = (1, 2)


_t = list(filter(lambda x: x[0] != Direction.UP, _permutations))
print(f'_t {_t} len(_t) {len(_t)}')

memory = {key: None for key in _t}
print(f'memory {memory}')

fill_distance(pos, memory)

# print(f'memory {memory}')
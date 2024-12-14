import sys

sys.setrecursionlimit(31209)


# logger slightly slow down the script, uncomment print for debug



def transform(lines):
    lines = [line.strip() for line in lines]
    for i, line in enumerate(lines):
        line = line.split(' ')
        position = line[0].replace('p=', '').split(',')
        position = (int(position[0]), int(position[1]))
        velocity = line[1].replace('v=', '').split(',')
        velocity = (int(velocity[0]), int(velocity[1]))
        lines[i] = (position, velocity)

    return lines


def move(w, h, i, j, x, y, target):
    new_i = i + x * target
    new_i = new_i % w
    new_j = j + y * target
    new_j = new_j % h
    # print(f'-> ({new_i}, {new_j}) ', end='')
    return (new_i, new_j)


def connectable(i, j, width, height, positions, visited=set()):
    # print(f'connectable({i}, {j}, {width}, {height}, positions, visited')
    count = 0

    if (i, j) in visited:
        return 0
    if (i, j) not in positions:
        return 0

    
    visited.add((i, j))
    
    count += 1
    

    directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for x, y in directions:
        if x < 0 or x >= height or y < 0 or y >= width:
            pass
        else:
            count += connectable(x, y, width, height, positions, visited)

    return count


def display(positions, width, height):
    for i in range(height):
        for j in range(width):
            if (j, i) in positions:
                print('。', end='')
            else:
                print('　', end='')
        print()


def solver(states, width, height):

    iter = 0
    while True:

        iter += 1
        print(f'iter {iter}')

        quadrants_1 = set()
        quadrants_2 = set()
        quadrants_3 = set()
        quadrants_4 = set()

        positions = set()

        for k, state in enumerate(states):
            # print(f'{iter}  move {state} ', end='')
            position = state[0]
            velocity = state[1]


            result = move(width, height, position[0], position[1], velocity[0], velocity[1], target=1)
            i, j = result
            states[k] = ((i, j), velocity)


            # width is odd and result on it
            if width % 2 != 0 and i == width // 2:
                # print('on mid, skipping')
                continue

            # height is odd and result on it
            if height % 2 != 0 and j == height // 2:
                # print('on mid, skipping')
                continue

            # upper
            if j < height // 2:
                if i < width // 2:
                    quadrants_1.add((i, j))
                    # print('at quadrant_1')
                else:
                    quadrants_2.add((i, j))
                    # print('at quadrant_2')
            else:
                if i < width // 2:
                    quadrants_3.add((i, j))
                    # print('at quadrant_3')
                else:
                    quadrants_4.add((i, j))
                    # print('at quadrant_4')
        
        positions = quadrants_1.union(quadrants_2).union(quadrants_3).union(quadrants_4)
        print(f'positions {len(positions)}')

        for x, y in positions:
            connectable_count = connectable(x, y, width, height, positions, visited=set())
            # print(f'position ({x}, {y})  connectable {connectable_count}')
            if connectable_count > 30:
                print(f'iter {iter} has position ({x}, {y})  connectable {connectable_count} > 30')
                display(positions, width, height)
                return iter
        else:
            continue
        break




width, height = 101, 103
states = transform(open('input'))
out = solver(states, width, height)
print(out)
assert out == 6644

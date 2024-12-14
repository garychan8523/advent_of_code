


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
    print(f'new ({new_i}, {new_j})')
    return (new_i, new_j)


def solver(states, width, height, target):

    quadrant_1 = 0
    quadrant_2 = 0
    quadrant_3 = 0
    quadrant_4 = 0

    for state in states:
        print(f'check {state}')
        position = state[0]
        velocity = state[1]


        result = move(width, height, position[0], position[1], velocity[0], velocity[1], target)
        i, j = result

        # width is odd and result on it
        if width % 2 != 0 and i == width // 2:
            print('on mid, skipping')
            continue

        # height is odd and result on it
        if height % 2 != 0 and j == height // 2:
            print('on mid, skipping')
            continue

        # upper
        if j < height // 2:
            if i < width // 2:
                quadrant_1 += 1
                print('quadrant_1')
            else:
                quadrant_2 += 1
                print('quadrant_2')
        else:
            if i < width // 2:
                quadrant_3 += 1
                print('quadrant_3')
            else:
                quadrant_4 += 1
                print('quadrant_4')

        print(f'quadrant_1 {quadrant_1}')
        print(f'quadrant_2 {quadrant_2}')
        print(f'quadrant_3 {quadrant_3}')
        print(f'quadrant_4 {quadrant_4}')


    return quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4 




width, height = 11, 7
states = transform(open('sample1_1'))
out = solver(states, width, height, target=5)
print(out)
assert out == 0


width, height = 11, 7
states = transform(open('sample'))
out = solver(states, width, height, target=100)
print(out)
assert out == 12


width, height = 101, 103
states = transform(open('input'))
out = solver(states, width, height, target=100)
print(out)
assert out == 224554908

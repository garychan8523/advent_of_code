

def transform(lines):
    lines = [line.strip() for line in lines]

    machines = []
    for i, line in enumerate(lines):
        if line.startswith('Button A'):
            button_a = lines[i]
            button_a = button_a.split(', ')
            a_x, a_y = int(button_a[0].replace('Button A: X+', '')), int(button_a[1].replace('Y+', ''))
            # print(f'splited A {button_a} {a_x} {a_y}')

            button_b = lines[i+1]
            button_b = button_b.split(', ')
            b_x, b_y = int(button_b[0].replace('Button B: X+', '')), int(button_b[1].replace('Y+', ''))
            # print(f'splited B {button_b} {b_x} {b_y}')

            prize = lines[i+2]
            prize = prize.split(', ')
            p_x, p_y = int(prize[0].replace('Prize: X=', '')), int(prize[1].replace('Y=', ''))
            # print(f'splited P {prize} {p_x} {p_y}')

            machines.append(((a_x, a_y), (b_x, b_y), (p_x, p_y)))
    return machines


# for linear equations
# c_1 * a + c_2 * b = p_1  (1)
# c_3 * a + c_4 * b = p_1  (2)
# we multiply (1) by c_3 and (2) by c_1 to let both first term cancel out each other
# then (1) second term - (2) second term will equals to (1) result - (2) result
# finally we divide the result by the coefficent on l.h.s. to get value of b thus a
# if (1) second term - (2) second term happens to be negative,
# (1) result - (2) result should also be negative so value of b should be >= 0 

def solver(machine):
    button_a, button_b, prize = machine[0], machine[1], machine[2]
    cost_a, cost_b = 3, 1
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize[0], prize[1]

    print(f'(({p_x} * {a_y}) - ({p_y} * {a_x})) / (({b_x} * {a_y}) - ({b_y} * {b_y}))')
    b_pressed = ((p_x * a_y) - (p_y * a_x)) / ((b_x * a_y) - (b_y * a_x))

    if b_pressed < 0 or not b_pressed.is_integer():
        return 0

    a_pressed = (p_x - b_x * b_pressed) / a_x

    if a_pressed < 0 or not a_pressed.is_integer():
        return 0

    print(f'a {a_pressed} b {b_pressed}')
    return int(cost_a * a_pressed) + int(cost_b * b_pressed)


out = 0
machines = transform(open('sample'))
for machine in machines:
    token = solver(machine)
    print(f'token {token}')
    if token != float('inf'):
        out += token
print(out)
assert out == 480

out = 0
machines = transform(open('input'))
for machine in machines:
    token = solver(machine)
    print(f'token {token}')
    if token != float('inf'):
        out += token
print(out)
assert out == 37680

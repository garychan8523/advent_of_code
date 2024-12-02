lines = open('13_2.in', 'r')

inputs = []
t = []
for line in lines:
    line = line.strip()
    if len(line) > 0:
        t.append(line.strip())
    else:
        inputs.append(t)
        t = []

print(f'inputs\n{inputs}\n')

v = []
h = []

for input in inputs:



    for i in range(len(input)-1):
        hi, lo = i, i+1

        mirror = True
        while hi != 0 or lo != len(input):
            print(f'[{i} {hi} {lo}]  compare {input[hi]} {input[lo]}')
            if input[hi] != input[lo]:
                mirror = False
                break
            if hi-1 >= 0:
                hi -= 1
            else:
                break
            if lo+1 < len(input):
                lo += 1
            else:
                break
        if mirror:
            print(f'i {i+1}')
            h.append(i+1)
            break


    input = list(map(list, zip(*input)))
    for i in range(len(input)-1):
        hi, lo = i, i+1

        mirror = True
        while hi != 0 or lo != len(input):
            print(f'[{i} {hi} {lo}]  compare {input[hi]} {input[lo]}')
            if input[hi] != input[lo]:
                mirror = False
                break
            if hi-1 >= 0:
                hi -= 1
            else:
                break
            if lo+1 < len(input):
                lo += 1
            else:
                break
        if mirror:
            print(f'i {i+1}')
            v.append(i+1)
            break

print(f'v {v}')
print(f'h {h}')
print(sum(v)+sum(h)*100)
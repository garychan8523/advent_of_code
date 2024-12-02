lines = open('file_to_lists.in', 'r')

out = []

for line in lines:
    line = line.strip()
    #print(line)
    # line = [int(_) for _ in line.split(' ')]
    line = [_ for _ in line]
    line = ''.join(line)
    out.append(line)

print(out)
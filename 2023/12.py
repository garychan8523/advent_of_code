input = ['.??..??...?##.', (1,1,3)]

row = input[0]
config = input[1]

row_splits = row
row_splits_index = []

while '..' in row_splits:
    row_splits = row_splits.replace('..', '.')
    row_splits = row_splits.split('.')
    row_splits = list(filter(lambda x: x != '', row_splits))

i = 0
for row_split in row_splits:
    print(f'row[i:] {row[i:]}')
    t = row[i:].find(row_split)
    row_splits_index.append((t+i, t+i+len(row_split)-1))
    i = t+len(row_split)


print(f'row\n{row}\n')
print(f'config\n{config}\n')
print(f'row_splits\n{row_splits}\n')
print(f'row_splits_index\n{row_splits_index}\n')

for i in range(len(row_splits)):
    coordinate = row_splits_index[i]
    left, right, length = coordinate[0], coordinate[1], len(row_splits[i])
    left = 0 if left-1 < 0 else left-1
    right = length+2 if length+2 < len(row) else length+1
    right += left
    segment = row[left:right]

    

    print(f'segment {segment} left {left}, right {right}')
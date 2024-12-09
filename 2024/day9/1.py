import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')



def transform(lines):
    lines = [line.strip() for line in lines]
    lines = [list(line) for line in lines]
    for i in range(len(lines)):
        lines[i] = [int(item) for item in lines[i]]
    return lines



def get_encode(files, free_space):
    out = []
    for i in range(len(files)):
        id = files[i][0]
        no_of_item = files[i][1]
        for j in range(no_of_item):
            out.append((id,))
        if i < len(free_space):
            for j in range(free_space[i]):
                out.append(('.',))
    return out



def compactable(free_space_indexes, i):
    return free_space_indexes[0] < i

def get_leftmost(free_space_indexes):
    return free_space_indexes.pop(0)

def get_checksum(encode):
    out = 0
    counter = 0
    for i in range(len(encode)):
        if encode[i] != ('.',):
            out += counter * int(encode[i][0])
            counter += 1
    return out

def solver(disk_map):
    logger.debug(f'disk_map {disk_map}')

    files = []
    free_space = []

    toggle = True
    id = 0
    for item in disk_map:
        if toggle:
            files.append((id, item))
            id += 1
        else:
            free_space.append(item)
        toggle = not toggle
    
    logger.debug(f'files {files}')
    logger.debug(f'free_space {free_space}')

    encode = list(get_encode(files, free_space))
    logger.debug(f'encode {encode}')

    free_space_indexes = []
    for i in range(len(encode)):
        if encode[i] == ('.',):
            free_space_indexes.append(i)
    logger.debug(f'free_space_indexes {free_space_indexes}')

    logger.debug(f'start {len(encode)}')
    for i in range(len(encode)-1, -1, -1):
        if encode[i] == ('.',):
            continue
        if not compactable(free_space_indexes, i):
            break
        leftmost_freespace_index = get_leftmost(free_space_indexes)
        encode[leftmost_freespace_index], encode[i] = encode[i], encode[leftmost_freespace_index]
    logger.debug('end')

    logger.debug(f'encode after {encode}')

    checksum = get_checksum(encode)

    logger.debug(f'checksum {checksum}')

    logger.debug(f'after compact {encode}')
    return (encode, checksum)




lines = transform(open('sample1'))
encode, checksum = solver(lines[0])
print(f'checksum {checksum}')
assert checksum == 60


lines = transform(open('sample'))
encode, checksum = solver(lines[0])
print(f'checksum {checksum}')
assert checksum == 1928

lines = transform(open('input'))
encode, checksum = solver(lines[0])
print(f'checksum {checksum}')
assert checksum == 6216544403458

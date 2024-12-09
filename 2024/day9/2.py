import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')



def transform(lines):
    lines = [line.strip() for line in lines]
    lines = [list(line) for line in lines]
    for i in range(len(lines)):
        lines[i] = [int(item) for item in lines[i]]
    return lines


def get_checksum(files):
    out = 0
    for file in files:
        file_id = file[0]
        file_start, file_end = file[1][0], file[1][1]
        for i in range(file_start, file_end+1):
            out += file_id * i
    return out


def merge_ranges(ranges):
    i = 0
    while i < len(ranges)-1:
        current_start, current_end = ranges[i][0], ranges[i][1]
        next_start, next_end = ranges[i+1][0], ranges[i+1][1]
        if next_start-current_end == 1:
            ranges[i] = (current_start, next_end)
            del ranges[i+1]
            continue
        i += 1


def swap(files, frees, file, free):
    logger.debug('swap')
    file_id = file[0]
    file_start, file_end = file[1][0], file[1][1]
    file_size = file_end-file_start+1

    free_start, free_end = free[0], free[1]
    free_size = free_end - free_start + 1

    for free_position in range(len(frees)):
        if frees[free_position] == free:
            break
    
    if file_size == free_size:
        frees.remove(free)
        files.remove(file)

        insert_index = -1
        for i in range(len(files)):
            if files[i][1][1] < free_start:
                insert_index = i+1
        files.insert(insert_index, (file_id, (free_start, free_end)))
        logger.debug(f'insert_index {insert_index} {(file_id, (free_start, free_end))}')

        insert_index = -1
        for i in range(len(frees)):
            if frees[i][1] < file_start:
                insert_index = i+1
            else:
                break
        if insert_index < 0:
            insert_index = 0
        frees.insert(insert_index, (file_start, file_end))
        merge_ranges(frees)
        logger.debug(f'frees insert_index {insert_index} {(file_start, file_end)}')
    else:
        # free_size > file_size
        frees.remove(free)
        # frees.append((file_start, file_end))
        files.remove(file)

        insert_index = -1
        for i in range(len(files)):
            if files[i][1][1] < free_start:
                insert_index = i+1
        files.insert(insert_index, (file_id, (free_start, free_start+file_size-1)))
        logger.debug(f'files insert_index {insert_index} {(file_id, (free_start, free_start+file_size-1))}')

        insert_index = -1
        for i in range(len(frees)):
            if frees[i][1] < file_start:
                insert_index = i+1
            else:
                break
        if insert_index < 0:
            insert_index = 0
        frees.insert(insert_index, (file_start, file_end))
        merge_ranges(frees)
        logger.debug(f'frees insert_index {insert_index} {(file_start, file_end)}')

        new_free_start = free_start+file_size
        insert_index = -1
        for i in range(len(frees)):
            if frees[i][1] < new_free_start:
                insert_index = i+1
            else:
                break
        if insert_index < 0:
            insert_index = 0
        frees.insert(insert_index, (new_free_start, free_end))
        merge_ranges(frees)
        logger.debug(f'frees insert_index {insert_index} {(new_free_start, free_end)}')
    
    logger.debug(f'files {files}')
    logger.debug(f'frees {frees}')


def solver(disk_map):
    logger.debug(f'disk_map {disk_map}')

    files = []
    frees = []

    toggle = True
    id = 0
    index = 0
    for item in disk_map:
        if toggle:
            files.append((id, (index, index + item -1)))
            id += 1
        else:
            if item > 0:
                frees.append((index, index + item -1))
        index = index + item
        toggle = not toggle
    
    logger.debug(f'files {files}')
    logger.debug(f'frees {frees}')

    checked = set()
    while len(checked) != len(files):
        if len(checked) % 100 == 0:
            print(f'{len(checked)} / {len(files)}')
        for i in range(len(files)-1, -1, -1):
            file_id = files[i][0]
            if file_id in checked:
                continue
            else:
                checked.add(file_id)
            
            file_start, file_end = files[i][1][0], files[i][1][1]
            file_size = file_end-file_start+1
            logger.debug(f'check for {files[i]} size {file_size}')
            for j in range(len(frees)):
                free_start, free_end = frees[j][0], frees[j][1]
                free_size = free_end - free_start + 1
                logger.debug(f'aginst frees {frees[j]} size {free_size}')
                if free_start >= file_start:
                    break

                if free_size >= file_size:
                    swap(files, frees, files[i], frees[j])
                    break
            else:
                continue
            break
    

    logger.debug(f'files {files}')
    logger.debug(f'frees {frees}')
        
    checksum = get_checksum(files)
    return checksum





lines = transform(open('sample'))
checksum = solver(lines[0])
print(f'checksum {checksum}')
assert checksum == 2858

lines = transform(open('input'))
checksum = solver(lines[0])
print(f'checksum {checksum}')
assert checksum == 6237075041489

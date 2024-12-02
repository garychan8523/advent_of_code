lines = open('2.in', 'r')


def get_num(string):
    text = ''
    for char in string:
        if char.isnumeric():
            text += char
    return int(text)

def validate(config, batch):
    valid = True
    if 'red' in batch and batch['red'] > config['red']:
        valid = False
    if 'green' in batch and batch['green'] > config['green']:
        valid = False
    if 'blue' in batch and batch['blue'] > config['blue']:
        valid = False
    return valid

# red, green, blue cubes loaded
config = {'red': 12, 'green': 13, 'blue': 14}

valid_game_ids = []

for line in lines:
    line = line.strip()

    game_valid = True

    game_id = int(line.split(':')[0].replace('Game ', ''))
    batches = line.split(':')[1].replace(' ', '').split(';')
    for i in range(len(batches)):
        colors = batches[i].split(',')
        print(f'colors {colors}')
        out = {}
        for color in colors:
            if 'red' in color:
                out['red'] = get_num(color)
            if 'green' in color:
                out['green'] = get_num(color)
            if 'blue' in color:
                out['blue'] = get_num(color)
        batches[i] = out
    
    for batch in batches:
        if not validate(config, batch):
            game_valid = False
    
    if game_valid:
        valid_game_ids.append(game_id)

    print (f'game_id {game_id}, batches {batches}')

print(f'valid_game_ids {valid_game_ids}, sum(valid_game_ids) {sum(valid_game_ids)}')

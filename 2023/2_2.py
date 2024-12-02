lines = open('2_2.in', 'r')


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

output = []

for line in lines:
    line = line.strip()

    # initial states
    config = {'red': 0, 'green': 0, 'blue': 0}

    game_id = int(line.split(':')[0].replace('Game ', ''))
    batches = line.split(':')[1].replace(' ', '').split(';')
    for i in range(len(batches)):
        colors = batches[i].split(',')
        print(f'colors {colors}')
        for color in colors:
            if 'red' in color and get_num(color) > config['red']:
                config['red'] = get_num(color)
            if 'green' in color and get_num(color) > config['green']:
                config['green'] = get_num(color)
            if 'blue' in color and get_num(color) > config['blue']:
                config['blue'] = get_num(color)
    
    output.append(config['red'] * config['green'] * config['blue'])

    print (f'game_id {game_id}, batches {batches}')

print(f'sum(output) {sum(output)}')

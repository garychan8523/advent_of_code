import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')



def get_rule_dict(rules):
    out = {}
    for rule in rules:
        splited = rule.split('|')
        splited[0], splited[1] = int(splited[0]), int(splited[1])
        if splited[0] not in out:
            out[splited[0]] = {splited[1]}
        else:
            out[splited[0]].add(splited[1])
    return out


def copy_without_index(_list, index):
    return [_list[i] for i in range(len(_list)) if i != index]


def is_correct(currents, remains, rules):
    logger.debug(f'is_correct {currents} {remains}')

    if len(currents) > 0:
        for i in range(len(currents)-1):
            current = currents[i]
            rest = currents[i+1:]+remains
            logger.debug(f'current {current} rest {rest}')
            if current not in rules:
                logger.debug(f'{currents} incorrect, current not in rules')
                return False
            else:
                _set = rules[current]
                for item in rest:
                    if item not in _set:
                        logger.debug(f'{currents} incorrect, {item} not in set {_set}')
                        return False


    # every item exists in rules and in correct order, no more remain
    if len(remains) == 0:
        logger.debug(f'{currents} correct, no more remains')
        return currents
    
    # otherwise, backtrack all possibilities
    # permutate currents+remains[i]+remains[j]+remains[k] ...
    # where i are remain elements, j are the remain elements without remains[i] etc
    for i in range(len(remains)):
        out = is_correct(currents+[remains[i]], copy_without_index(remains, i), rules)
        if out != False:
            return out
    
    return False


def get_rules_updates(lines):
    rules = []
    updates = []

    target = rules
    for line in lines:
        if len(line) != 0:
            target.append(line)
        if len(line) == 0:
            target = updates
    
    for i in range(len(updates)):
        updates[i] = updates[i].split(',')
        updates[i] = [int(i) for i in updates[i]]

    rule_dict = get_rule_dict(rules)

    return (rule_dict, updates)




total = 0
lines = open('sample')
lines = [line.strip() for line in lines]

rules, updates = get_rules_updates(lines)

logger.debug(f'rules {rules}')
logger.debug(f'updates {updates}')

for update in updates:
    logger.debug(f'checking update {update}')
    if is_correct(update, [], rules):
        logger.debug(f'{update} is correct, skipping ...')
        continue
    else:
        logger.debug(f'{update} is incorrect, trying ...')
        out = is_correct([], update, rules)
        if out != False:
            logger.debug(f'> out {out}')
            total += out[len(out)//2]

print(total)
assert total == 123



total = 0
lines = open('input')
lines = [line.strip() for line in lines]

rules, updates = get_rules_updates(lines)

logger.debug(f'rules {rules}')
logger.debug(f'updates {updates}')

for update in updates:
    logger.debug(f'checking update {update}')
    if is_correct(update, [], rules):
        logger.debug(f'{update} is correct, skipping ...')
        continue
    else:
        logger.debug(f'{update} is incorrect, trying ...')
        out = is_correct([], update, rules)
        if out != False:
            logger.debug(f'> out {out}')
            total += out[len(out)//2]

print(total)
assert total == 4743

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


def is_correct(update, rules):
    if len(updates) == 0:
        return True
    
    lookup = rules
    for i in range(len(update)-1):
        page = update[i]
        logger.debug(f'checking {page} lookup {lookup}')
        if page not in lookup:
            return False
        else:
            if page not in rules:
                return False
            else:
                lookup = rules[page]

    return True


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
    out = is_correct(update, rules)
    logger.debug(f'{update} {out}')
    if out:
        total += update[len(update)//2]
    logger.debug('')

print(total)
assert total == 143


total = 0
lines = open('input')
lines = [line.strip() for line in lines]

rules, updates = get_rules_updates(lines)

logger.debug(f'rules {rules}')
logger.debug(f'updates {updates}')

for update in updates:
    out = is_correct(update, rules)
    logger.debug(f'{update} {out}')
    if out:
        total += update[len(update)//2]
    logger.debug('')

print(total)
assert total == 5651

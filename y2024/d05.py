import itertools
import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 5")
    lines = [line.strip() for line in open(r'y2024\data\05.txt')]
    # lines = [line.strip() for line in open(r'y2024\data\05.example.txt')]

    # Part 1
    time_0 = time.time()

    rules = []
    updates = []

    rules_done = False
    for line in lines:
        if line == '':
            rules_done = True
            continue

        if not rules_done:
            (a,b) = (int(x) for x in line.split('|'))
            rules.append((a, b))
        else:
            updates.append([int(x) for x in line.split(',')])

    def is_valid(update):
        valid = True
        for k in range(1, len(update)):
            u = update[k]
            for p in update[:k]:
                if not (p, u) in rules:
                    valid = False
                    break
            if not valid:
                break
        return valid

    valid_updates = []
    for update in updates:
        if is_valid(update):
            valid_updates.append(update)

    s = 0
    for update in valid_updates:
        s += update[int((len(update)-1)/2)]

    print_complete(time_0, s)

    # Part 2
    time_0 = time.time()

    corrected_updates = []
    for update in updates:
        valid = True
        invalid = []
        for k in range(1, len(update)):
            u = update[k]
            for p in update[:k]:
                if not (p, u) in rules:
                    valid = False
                    invalid.append(u)
                    break
        if not valid:
            for i in invalid:
                update.remove(i)
            for i in invalid:
                for k in range(len(update)+1):
                    cand = update[:k] + [i] + update[k:]
                    if is_valid(cand):
                        update = cand
                        break
            corrected_updates.append(update)

    s = 0
    for update in corrected_updates:
        s += update[int((len(update)-1)/2)]

    print_complete(time_0, s)

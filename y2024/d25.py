import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 25")
    data = ''.join(x.strip() if x.strip() != '' else x for x in open(r'y2024\data\25.txt'))
    # data = ''.join(x.strip() if x.strip() != '' else x for x in open(r'y2024\data\25.example.txt'))

    keys = []
    locks = []
    for item in data.split('\n'):
        col = [''.join([item[m + k * 5] for k in range(1, 6)]).count('#') for m in range(5)]
        if item.startswith('#####'):
            locks.append(col)
        else:
            keys.append(col)

    # Part 1
    time_0 = time.time()

    res = []
    for lock in locks:
        for key in keys:
            res.append(1 if all([x + y <= 5 for x, y in zip(key, lock)]) else 0)

    print_complete(time_0, sum(res))

    # Part 2
    time_0 = time.time()

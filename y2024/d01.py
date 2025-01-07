import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 1")
    data = [line.strip().split() for line in open(r'y2024\data\01.txt')]
    # data = [line.strip().split() for line in open(r'y2024\data\01.example.txt')]

    # Part 1
    time_0 = time.time()

    l1 = [int(x) for x, y in data]
    l2 = [int(y) for x, y in data]

    l1.sort()
    l2.sort()

    s = 0
    for k in range(len(l1)):
        s += abs(l1[k] - l2[k])

    print_complete(time_0, s)

    # Part 2
    time_0 = time.time()

    s = 0
    for k in l1:
        s += k * l2.count(k)

    print_complete(time_0, s)

import time
import numpy

from AoCutils.utils import print_complete


def run():
    print("2024, day 2")
    lines = [list(map(int, line.strip().split())) for line in open(r'y2024\data\02.txt')]
    # lines = [list(map(int, line.strip().split())) for line in open(r'y2024\data\02.example.txt')]

    def is_safe(l):
        d = numpy.diff(l)
        limited = all([1 <= abs(x) <= 3 for x in d])
        monotone = all([x > 0 for x in d]) or all([x < 0 for x in d])
        return limited and monotone


    # Part 1
    time_0 = time.time()

    s = 0
    unsafe = []
    for l in lines:
        if is_safe(l):
            s += 1
        else:
            unsafe.append(l)

    print_complete(time_0, s)

    # Part 2
    time_0 = time.time()

    for l in unsafe:
        for k in range(len(l)):
            cand = l[:k] + l[k+1:]
            if is_safe(cand):
                s += 1
                break

    print_complete(time_0, s)

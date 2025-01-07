import functools
import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 19")
    lines = [line.strip() for line in open(r'y2024\data\19.txt')]
    # lines = [line.strip() for line in open(r'y2024\data\19.example.txt')]

    patterns = [x.strip() for x in lines[0].split(',')]
    designs = []
    for line in lines[2:]:
        designs.append(line)

    @functools.cache
    def is_possible(design):
        count = 0
        for pattern in patterns:
            if design == pattern:
                count += 1
            elif design.startswith(pattern):
                count += is_possible(design[len(pattern):])
        return count

    # Part 1
    time_0 = time.time()

    a = 0
    b = 0
    for design in designs:
        r = is_possible(design)
        b += r
        if r > 0:
            a += 1

    print_complete(time_0, a)

    # Part 2
    time_0 = time.time()

    print_complete(time_0, b)

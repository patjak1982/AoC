import time
from AoCutils.utils import print_complete


def run():
    print("2024, day 6 (very time consuming)")
    lines = [line.strip() for line in open(r'y2024\data\06.txt')]
    lines = [line.strip() for line in open(r'y2024\data\06.example.txt')]

    nx = len(lines[0])
    ny = len(lines)

    obstacles = set()
    guard = None
    for yi, line in enumerate(lines):
        for xi, c in enumerate(line):
            if c == '#':
                obstacles.add(xi + yi*1j)
            elif c == '^':
                guard = [xi + yi*1j, -1*1j]
    guard_0 = guard.copy()

    # Part 1
    time_0 = time.time()

    trace = set()
    trace.add(guard[0])

    while True:
        test_pos = guard[0] + guard[1]
        if test_pos not in obstacles:
            guard[0] += guard[1]
        else:
            guard[1] *= 1j

        if 0 <= test_pos.real < nx and 0 <= test_pos.imag < ny: # Inside area
            trace.add(guard[0])
        else:
            break

    print_complete(time_0, len(trace))

    # Part 2
    time_0 = time.time()

    positions = list()
    c = 0
    for cand in trace:
        c += 1
        # print(c, len(trace))
        guard = guard_0.copy()
        states = list()
        while True:
            test_pos = guard[0] + guard[1]
            if test_pos in obstacles or test_pos == cand:
                guard[1] *= 1j
            else:
                guard[0] += guard[1]

            if 0 <= test_pos.real < nx and 0 <= test_pos.imag < ny:  # Inside area
                if guard in states: # Have we already been here?
                    positions.append(cand)
                    break
                states.append(guard.copy())
            else:
                break

    print_complete(time_0, len(positions))
    # 1812 is correct

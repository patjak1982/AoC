import time
from itertools import combinations

from AoCutils.utils import print_complete


def run():
    print("2024, day 8")
    lines = [line.strip() for line in open(r'y2024\data\08.txt')]
    #lines = [line.strip() for line in open(r'y2024\data\08.example.txt')]

    frequencies = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            c = lines[y][x]
            if c != '.':
                if c in frequencies:
                    frequencies[c].append((x, y))
                else:
                    frequencies[c] = [(x, y)]

    nx = len(lines[0])
    ny = len(lines)

    # Part 1
    time_0 = time.time()

    antinodes = set()
    for frequency in frequencies:
        combs = list(combinations(frequencies[frequency], 2))
        for comb in combs:
            dx = comb[1][0]-comb[0][0]
            dy = comb[1][1]-comb[0][1]
            antinode1 = (comb[0][0] - dx, comb[0][1] - dy)
            antinode2 = (comb[1][0] + dx, comb[1][1] + dy)
            if antinode1 not in antinodes:
                antinodes.add(antinode1)
            if antinode2 not in antinodes:
                antinodes.add(antinode2)

    c = 0
    for antinode in antinodes:
        if 0 <= antinode[0] < nx and 0 <= antinode[1] < ny:
            c += 1

    print_complete(time_0, c)

    # Part 2
    time_0 = time.time()

    antinodes = set()
    for frequency in frequencies:
        combs = list(combinations(frequencies[frequency], 2))
        for comb in combs:
            dx = comb[1][0]-comb[0][0]
            dy = comb[1][1]-comb[0][1]
            node0 = comb[0]

            antinodes.add(node0)

            k = 1
            while True:
                cnode_x = node0[0] + k*dx
                cnode_y = node0[1] + k*dy

                if 0 <= cnode_x < nx and 0 <= cnode_y < ny:
                    antinodes.add((cnode_x, cnode_y))
                    k += 1
                else:
                    break
            k = -1
            while True:
                cnode_x = node0[0] + k*dx
                cnode_y = node0[1] + k*dy

                if 0 <= cnode_x < nx and 0 <= cnode_y < ny:
                    antinodes.add((cnode_x, cnode_y))
                    k -= 1
                else:
                    break

    c = 0
    for antinode in antinodes:
        if 0 <= antinode[0] < nx and 0 <= antinode[1] < ny:
            c += 1

    print_complete(time_0, c)

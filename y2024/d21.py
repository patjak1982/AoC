import functools
import time

import networkx as nx
import itertools

from AoCutils.utils import print_complete


def diff(l):
    return [y - x for x, y in zip(l[:-1], l[1:])]


def diff2d(l):
    return [x1 - x0 + (y1 - y0) * 1j for (x0, y0), (x1, y1) in zip(l[:-1], l[1:])]


def diff2c(d):
    if d == 1:
        return '>'
    elif d == -1:
        return '<'
    elif d == 1j:
        return 'v'
    elif d == -1j:
        return '^'
    print("ERROR", d)


def solve(pattern, keypad):
    G = nx.grid_2d_graph(len(keypad[0]), len(keypad))
    positions = {}
    pos = None
    for yi, line in enumerate(keypad):
        for xi, c in enumerate(line):
            if c is not None:
                positions[c] = (xi, yi)
                if c == 'A':
                    pos = (xi, yi)
            else:
                G.remove_node((xi, yi))
    solutions = []
    for p in pattern:
        solutions.append([])
        for path in nx.all_shortest_paths(G, pos, positions[p]):
            solutions[-1].append('')
            for d in diff2d(path):
                solutions[-1][-1] += diff2c(d)
            solutions[-1][-1] += 'A'
        pos = positions[p]

    sols = solutions[0].copy()
    for s in solutions[1:]:
        sols = [x + y for x, y in list(itertools.product(sols, s))]

    return sols


num_keypad = [
    ('7', '8', '9'),
    ('4', '5', '6'),
    ('1', '2', '3'),
    (None, '0', 'A')
]
dir_keypad = [
    (None, '^', 'A'),
    ('<', 'v', '>'),
]

def run():
    print("2024, day 21")
    lines = [x.strip() for x in open(r'y2024\data\21.txt')]
    # lines = [x.strip() for x in open(r'y2024\data\21.example.txt')]

    paths = {
        ('<', '<'): ['A'],
        ('<', '^'): ['>^A'],
        ('<', 'v'): ['>A'],
        ('<', 'A'): ['>^>A', '>>^A'],
        ('<', '>'): ['>>A'],
        ('^', '<'): ['v<A'],
        ('^', '^'): ['A'],
        ('^', 'v'): ['vA'],
        ('^', 'A'): ['>A'],
        ('^', '>'): ['v>A', '>vA'],
        ('v', '<'): ['<A'],
        ('v', '^'): ['^A'],
        ('v', 'v'): ['A'],
        ('v', 'A'): ['^>A', '>^A'],
        ('v', '>'): ['>A'],
        ('A', '<'): ['v<<A', '<v<A'],
        ('A', '^'): ['<A'],
        ('A', 'v'): ['v<A', '<vA'],
        ('A', 'A'): ['A'],
        ('A', '>'): ['vA'],
        ('>', '<'): ['<<A'],
        ('>', '^'): ['^<A', '<^A'],
        ('>', 'v'): ['<A'],
        ('>', 'A'): ['^A'],
        ('>', '>'): ['A']
    }

    @functools.cache
    def shortest_path_length(keys, level):
        if not level:
            return len(keys)

        length = 0
        for a, b in zip('A'+keys[:-1], keys):
            opt = 100000000000000000
            for path in paths[(a, b)]:
                c = shortest_path_length(path, level-1)
                opt = min(opt, c)
            length += opt
        return length

    # Part 1
    time_0 = time.time()
    s = 0
    for code in lines:
        solutions = solve(code, num_keypad)
        shortest = min([shortest_path_length(solution, 2) for solution in solutions])
        s += shortest * int(code[:-1])
    print_complete(time_0, s)

    # Part 2
    time_0 = time.time()
    s = 0
    for code in lines:
        solutions = solve(code, num_keypad)
        shortest = min([shortest_path_length(solution, 25) for solution in solutions])
        s += shortest * int(code[:-1])
    print_complete(time_0, s)

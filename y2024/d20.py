import time
import itertools
import networkx as nx

from AoCutils.utils import print_complete


def run():
    print("2024, day 20")
    lines = [x.strip() for x in open(r'y2024\data\20.txt')]
    # lines = [x.strip() for x in open(r'y2024\data\20.example.txt')]

    G = nx.grid_2d_graph(len(lines[0]), len(lines))

    p_s = None
    for yi, y in enumerate(lines):
        for xi, x in enumerate(y):
            if x == '#':
                G.remove_node((xi, yi))
            elif x == 'S':
                p_s = (xi, yi)

    sp = nx.single_source_dijkstra_path_length(G, p_s)

    def d(n1, n2):
        return abs(n1[0]-n2[0]) + abs(n1[1]-n2[1])

    # Part 1
    time_0 = time.time()
    diff_a = {}
    diff_b = {}
    for c in itertools.combinations(sp, 2):
        na, nb = c
        da = sp[na]
        db = sp[nb]
        dab_nom = abs(da-db)
        dab_cheat = d(na, nb)
        delta = dab_nom - dab_cheat
        if delta >= 100:
            if dab_cheat == 2:
                if delta in diff_a:
                    diff_a[delta] += 1
                else:
                    diff_a[delta] = 1
            if 2 <= dab_cheat <= 20:
                if delta in diff_b:
                    diff_b[delta] += 1
                else:
                    diff_b[delta] = 1

    print_complete(time_0, sum([diff_a[x] for x in diff_a]))
    print_complete(time_0, sum([diff_b[x] for x in diff_b]))

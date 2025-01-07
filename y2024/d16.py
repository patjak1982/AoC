import time

import networkx as nx

from AoCutils.utils import print_complete


def run():
    print("2024, day 16")
    lines = [line.strip() for line in open(r'y2024\data\16.txt')]
    # lines = [line.strip() for line in open(r'y2024\data\16.example.txt')]

    p_s = None
    p_e = None
    
    G = nx.DiGraph()
    
    for yi, line in enumerate(lines):
        for xi, c in enumerate(line):
            if c == '#':
                continue
            if c == 'E':
                p_e = xi + 1j * yi
            elif c == 'S':
                p_s = (xi + 1j * yi, 1)
            G.add_node((xi + 1j * yi, 1))
            G.add_node((xi + 1j * yi, -1))
            G.add_node((xi + 1j * yi, 1j))
            G.add_node((xi + 1j * yi, -1j))
    
    for n, d in G.nodes():
        G.add_edge((n, d), (n, d * 1j), weight=1000)
        G.add_edge((n, d), (n, d * -1j), weight=1000)
        if (n + d, d) in G.nodes():
            G.add_edge((n, d), (n + d, d), weight=1)
            
    G.add_edge((p_e, 1), "END", weight=0)
    G.add_edge((p_e, -1), "END", weight=0)
    G.add_edge((p_e, 1j), "END", weight=0)
    G.add_edge((p_e, -1j), "END", weight=0)

    # Part 1
    time_0 = time.time()

    p = nx.shortest_path(G, p_s, "END", weight="weight")
    
    cost = 0
    dp = p_s[1]
    for n in p:
        if n == "END":
            continue
        n, d = n
        if n == p_e:
            break
        if d != dp:
            dp = d
            cost += 1000
        else:
            cost += 1

    print_complete(time_0, cost)
        
    # Part 2
    time_0 = time.time()

    p = set()
    for path in nx.all_shortest_paths(G, p_s, "END", weight="weight"):
        for n, _ in path[:-1]:
           p.add(n)
            
    print_complete(time_0, len(p))

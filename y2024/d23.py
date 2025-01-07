import time
import networkx as nx

from AoCutils.utils import print_complete


def run():
    print("2024, day 23")
    lines = [line.strip() for line in open(r'y2024\data\23.txt')]
    #lines = [line.strip() for line in open(r'y2024\data\23.example.txt')]

    G = nx.Graph()

    for line in lines:
        a, b = line.split('-')
        if not a in G.nodes():
            G.add_node(a)
        if not b in G.nodes():
            G.add_node(b)
        G.add_edge(a, b)

    # Part 1
    time_0 = time.time()

    cliques = [x for x in nx.enumerate_all_cliques(G) if len(x) == 3]

    cnt = 0
    for (a,b,c) in cliques:
        if 't' in [a[0], b[0], c[0]]:
            #print(a, b, c)
            cnt += 1

    print_complete(time_0, cnt)

    # Part 2
    time_0 = time.time()
    cmax = 0
    password = ''
    for c in nx.find_cliques(G):
        if len(c) > cmax:
            cmax = len(c)
            c.sort()
            password = c
    password = ','.join(password)

    print_complete(time_0, password)

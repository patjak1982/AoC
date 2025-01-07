import time

import networkx as nx

from AoCutils.utils import print_complete


def run():
    print("2024, day 18")
    lines = [line.strip().split(',') for line in open(r'y2024\data\18.txt')]
    # lines = [line.strip().split(',') for line in open(r'y2024\data\18.example.txt')]

    data = [(int(x), int(y)) for x,y in lines]
    xmax = max(x for x, _ in data)
    ymax = max(y for _, y in data)

    G = nx.Graph()
    for y in range(ymax+1):
        for x in range(xmax+1):
            if (x, y) not in data[:1024]:
                G.add_node((x, y))
                if (x-1, y) in G.nodes:
                    G.add_edge((x, y), (x-1,y))
                if (x, y-1) in G.nodes:
                    G.add_edge((x, y), (x,y-1))

    # Part 1
    time_0 = time.time()

    sp = nx.shortest_path(G, (0, 0), (xmax, ymax))

    print_complete(time_0, len(sp)-1)

    # Part 2
    time_0 = time.time()

    for c in range(1024, len(data)):
        G.remove_node(data[c])
        if not nx.has_path(G, (0, 0), (xmax, ymax)):
            break

    print_complete(time_0, ','.join(map(str, data[c])))

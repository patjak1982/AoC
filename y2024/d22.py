import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 22")
    lines = map(int, [line.strip() for line in open(r'y2024\data\22.txt')])
    #lines = map(int, [line.strip() for line in open(r'y2024\data\22.example.txt')])

    buyers = [[l] for l in lines]

    def nxt(c):
        r = c ^ ((c << 6) & 0xFFFFFF)
        r ^= (r >> 5) & 0xFFFFFF
        return r ^ (r << 11) & 0xFFFFFF

    # Part 1
    time_0 = time.time()

    # Generate all secret numbers
    for bi in range(len(buyers)):
        for _ in range(2000):
            buyers[bi].append(nxt(buyers[bi][-1]))

    s = sum([b[-1] for b in buyers])
    print_complete(time_0, s)

    # Part 2
    time_0 = time.time()
    def diff(l):
        n = len(l)
        return [l[k + 1] - l[k] for k in range(n - 1)]

    results = {}
    for buyer in buyers:
        s = [x % 10 for x in buyer]
        d = diff(s)
        deltas = set()
        for k in range(2000-4+1):
            dc = tuple(d[k:(k + 4)])
            if dc not in deltas:
                deltas.add(dc)
                if dc not in results:
                    results[dc] = 0
                results[dc] += s[k + 4]

    m = 0
    for k in results:
        if results[k] > m:
            m = results[k]
    s = max(results.values())

    print_complete(time_0, s)

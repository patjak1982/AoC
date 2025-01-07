# from collections import Counter
#
# with open("data\\11.txt") as f:
#     stones = Counter(map(int, f.read().split()))
#
# for blinks in range(1, 76):
#     new_stones = Counter()
#     for n, num_stone in stones.items():
#         if n == 0:
#             new_stones[1] += num_stone
#         elif len(s := str(n)) % 2 == 0:
#             for m in int(s[: len(s) // 2]), int(s[len(s) // 2 :]):
#                 new_stones[m] += num_stone
#         else:
#             new_stones[2024 * n] += num_stone
#     stones = new_stones
#     if blinks in (25, 75):
#         print(sum(new_stones.values()))
import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 11")
    stones = map(int, [x.strip().split() for x in open(r'y2024\data\11.txt')][0])
    # stones = map(int, [x.strip().split() for x in open(r'y2024\data\11.example.txt')][0])
    # stones = map(int, [x.strip().split() for x in open(r'y2024\data\11.example2.txt')][0])

    counts = {}
    for stone in stones:
        counts[stone] = 1

    def calc(counts, n):
        for _ in range(n):
            oldcounts = counts.copy()
            counts = {}

            for c in oldcounts:
                if c == 0:
                    # print(counts)
                    if 1 in counts:
                        counts[1] += oldcounts[0]
                    else:
                        counts[1] = oldcounts[0]
                else:
                    sc = str(c)
                    if len(sc) % 2 == 0:
                        l = int(len(sc) / 2)
                        a, b = int('0'+sc[:l]), int('0'+sc[l:])
                        for x in [a, b]:
                            if x in counts:
                                counts[x] += oldcounts[c]
                            else:
                                counts[x] = oldcounts[c]
                    else:
                        n = 2024 * c
                        if n in counts:
                            counts[n] += oldcounts[c]
                        else:
                            counts[n] = oldcounts[c]
            s = 0
            for k in counts:
                s += counts[k]
        return sum([counts[c] for c in counts])

    # Part 1
    time_0 = time.time()
    print_complete(time_0, calc(counts, 25))

    # Part 2
    time_0 = time.time()
    print_complete(time_0, calc(counts, 75))

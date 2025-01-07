import time
import re
from AoCutils.utils import print_complete


def run():
    print("2024, day 14")
    lines = [line.strip() for line in open(r'y2024\data\14.txt')]
    #lines = [line.strip() for line in open(r'y2024\data\14.example.txt')]

    robots = []
    for line in lines:
        m = re.match(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)", line)
        px, py, vx, vy = map(int, m.groups())
        robots.append([px, py, vx, vy])
    robots_orig = robots.copy()

    nr = len(robots)
    nx = 0
    ny = 0
    for px, py, _, _ in robots:
        nx = max(nx, px + 1)
        ny = max(ny, py + 1)

    def print_r():
        for y in range(ny):
            l = ''
            for x in range(nx):
                cnt = 0
                for rx, ry, _, _ in robots:
                    if rx == x and ry == y:
                        cnt += 1
                if cnt == 0:
                    l += '.'
                else:
                    l += str(cnt)
            print(l)

    def step():
        for ri in range(len(robots)):
            px, py, vx, vy = robots[ri]
            robots[ri][0] = (px + vx) % nx
            robots[ri][1] = (py + vy) % ny

    # Part 1
    time_0 = time.time()

    for _ in range(100):
        step()

    qix = int((nx + 1*0) / 2)
    qiy = int((ny + 1*0) / 2)

    sx = [list(range(qix)), list(range(qix + 1, nx))]
    sy = [list(range(qiy)), list(range(qiy + 1, ny))]

    safety_factor = 1
    for ry in sy:
        for rx in sx:
            cnt = 0
            for x in rx:
                for y in ry:
                    for px, py, _, _ in robots:
                        if px == x and py == y:
                            cnt += 1
            #print(rx, ry, cnt)
            safety_factor *= cnt

    print_complete(time_0, safety_factor)

    # Part 2
    time_0 = time.time()
    means = []
    vars = []
    N = 10000

    minvar = (0, 100000000000)

    for k in range(N):
        step()

        mean = [sum(x for x, _, _, _ in robots) / nr,
                sum(y for _, y, _, _ in robots) / nr]
        var = [sum((x-mean[0])**2 for x, _, _, _ in robots) / (nr - 1),
               sum((y-mean[1])**2 for _, y, _, _ in robots) / (nr - 1)]

        means.append(mean)
        vars.append(var)

        if sum(var) < minvar[1]:
            minvar = (k+101, sum(var))

    print_complete(time_0, minvar[0])

import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 4")
    lines = [line.strip() for line in open(r'y2024\data\04.txt')]
    # lines = [line.strip() for line in open(r'y2024\data\04.example.txt')]

    N_rows = len(lines)
    N_cols = len(lines[0])

    # Part 1
    time_0 = time.time()

    # transpose
    lines_t = []
    for m in range(N_cols):
        lines_t.append('')
        for k in range(N_rows):
            lines_t[-1] += lines[k][m]

    # diag 1
    lines_d1 = []
    for c in range(N_cols,0,-1):
        lines_d1.append('')
        for i in range(min(N_cols-c, N_rows)):
            lines_d1[-1] += lines[i][c+i]
    for r in range(N_rows):
        lines_d1.append('')
        for i in range(min(N_rows-r, N_cols)):
            lines_d1[-1] += lines[r+i][i]

    # diag 2
    lines_d2 = []
    for c in range(N_cols):
        lines_d2.append('')
        for i in range(min(c, N_rows)+1):
            lines_d2[-1] += lines[i][c-i]
    for r in range(1, N_rows):
        lines_d2.append('')
        for i in range(min(N_rows-r, N_cols)):
            lines_d2[-1] += lines[r+i][N_cols-i-1]
            # print(r+i, N_cols-i-1)

    cnt = 0
    for line in lines+lines_t+lines_d1+lines_d2:
        cnt += line.count('XMAS')
        cnt += line.count('SAMX')

    print_complete(time_0, cnt)

    # Part 2
    time_0 = time.time()
    cnt = 0
    for r in range(N_rows-2):
        for c in range(N_cols-2):
            d1 = lines[r][c] + lines[r+1][c+1] + lines[r+2][c+2]
            d2 = lines[r+2][c] + lines[r+1][c+1] + lines[r][c+2]
            if d1 in ['MAS', 'SAM'] and d2 in ['MAS', 'SAM']:
                cnt += 1

    print_complete(time_0, cnt)

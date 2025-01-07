import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 13")
    lines = [line.strip() for line in open(r'y2024\data\13.txt')]
    # lines = [line.strip() for line in open(r'y2024\data\13.example.txt')]

    eqs = [[]]
    for line in lines:
        if not line:
            eqs.append([])
        else:
            if line.startswith('Button'):
                line = line.replace('X+', '')
                line = line.replace('Y+', '')
                line = line.replace(',', '')
                _, _, a,b = line.split()
                a = int(a)
                b = int(b)
                eqs[-1].append((a, b))
            else:
                line = line.replace('X=', '')
                line = line.replace('Y=', '')
                line = line.replace(',', '')
                _, a, b = line.split()
                a = int(a)
                b = int(b)
                eqs[-1].append((a, b))

    # Part 1
    time_0 = time.time()

    s = 0
    for eq in eqs:
        a, b = eq[0]
        c, d = eq[1]
        x, y = eq[2]

        A = d
        D = a
        B = -c
        C = -b
        det = a*d - c*b
        ca = int((x*A + y*B)/det)
        cb = int((x*C + y*D)/det)

        if a*ca+c*cb == x and b*ca+d*cb == y:
            c = 3*ca + cb
            s += c

    print_complete(time_0, s)

    # Part 2
    time_0 = time.time()

    s = 0
    for eq in eqs:
        a, b = eq[0]
        c, d = eq[1]
        x, y = eq[2]
        x += 10000000000000
        y += 10000000000000

        A = d
        D = a
        B = -c
        C = -b
        det = a*d - c*b
        ca = int((x*A + y*B)/det)
        cb = int((x*C + y*D)/det)

        if a*ca+c*cb == x and b*ca+d*cb == y:
            c = 3*ca + cb
            s += c

    print_complete(time_0, s)

import time
import re

from AoCutils.utils import print_complete


def run():
    print("2024, day 3")
    data = ''.join([line.strip() for line in open(r'y2024\data\03.txt')])
    #data = ''.join([line.strip() for line in open(r'y2024\data\03.example.txt')])

    memory = data[data.find('mul'):]
    args = [x for x in memory.split('mul') if x != '']
    validarg = re.compile(r'^\(\d+,\d+\)')

    # Part 1
    time_0 = time.time()

    s = 0
    for arg in args:
        m = validarg.match(arg)
        if m:
            m = m.group(0)
            (x,y) = eval(m)
            s += x*y
    print_complete(time_0, s)

    # Part 2
    time_0 = time.time()
    do = True

    s = 0
    for arg in args:
        m = validarg.match(arg)
        docount = arg.count('do()')
        dontcount = arg.count('don\'t()')
        if m:
            m = m.group(0)
            (x,y) = eval(m)
            if do:
                s += x*y

        if docount + dontcount > 1:
            continue
        elif docount == 1:
            do = True
        elif dontcount == 1:
            do = False
    print_complete(time_0, s)

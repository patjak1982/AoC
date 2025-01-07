import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 24")
    lines = [line.strip() for line in open(r'y2024\data\24.txt')]
    # lines = [line.strip() for line in open(r'y2024\data\24.example.txt')]

    wires = {}
    gates = []

    for line in lines:
        if ':' in line:
            a, b = line.split(': ')
            wires[a] = int(b)
        elif '->' in line:
            a, op, b, _, c = line.split()
            wires[c] = None
            gates.append((op, a, b, c))

    while gates:
        #all_found = True
        remaining = []
        for g in gates:
            (op, a, b, c) = g
            if wires[a] is not None and wires[b] is not None:
                if op == 'OR':
                    wires[c] = wires[a] | wires[b]
                elif op == 'AND':
                    wires[c] = wires[a] & wires[b]
                elif op == 'XOR':
                    wires[c] = wires[a] ^ wires[b]
            else:
                remaining.append(g)
        #print('w', wires)
        #print('r', remaining)
        #if all_found:
        #    break
        gates = remaining.copy()

    outputs = []
    for w in wires:
        if w.startswith('z'):
            outputs.append(w)
    outputs.sort(reverse=True)

    # Part 1
    time_0 = time.time()

    b_str = ''
    for o in outputs:
        b_str += str(wires[o])

    #print(wires)
    #print(gates)
    #print(outputs)
    #print(b_str)
    print_complete(time_0, int(b_str, 2))

def main2():
    lines = [x.strip() for x in open(r'data\24.txt')]
    #lines = [x.strip() for x in open(r'data\24.example.txt')]
    #lines = [x.strip() for x in open(r'data\24.example2.txt')]
    #lines = [x.strip() for x in open(r'data\24.example3.txt')]
    #lines = [x.strip() for x in open(r'data\24.example4.txt')]

    wires = {}
    gates = []

    for line in lines:
        if ':' in line:
            a, b = line.split(': ')
            wires[a] = int(b)
        elif '->' in line:
            a, op, b, _, c = line.split()
            wires[c] = None
            gates.append(op)
            gates.append(a)
            gates.append(b)
            gates.append(c)

    gates_o = gates.copy()
    print(gates)
    wires_o = wires.copy()

    def execute(ws, gs):
        while gs:
            remaining = []
            for gi in range(int(len(gs)/4)):
                (op, a, b, c) = gs[gi*4:gi*4+4]
                if ws[a] is not None and ws[b] is not None:
                    if op == 'OR':
                        ws[c] = ws[a] | ws[b]
                    elif op == 'AND':
                        ws[c] = ws[a] & ws[b]
                    elif op == 'XOR':
                        ws[c] = ws[a] ^ ws[b]
                else:
                    remaining += [op, a, b, c]
            gs = remaining.copy()

    xs = []
    ys = []
    zs = []
    for w in wires:
        if w.startswith('x'):
            xs.append(w)
        elif w.startswith('y'):
            ys.append(w)
        elif w.startswith('z'):
            zs.append(w)
    xs.sort(reverse=True)
    ys.sort(reverse=True)
    zs.sort(reverse=True)

    def get_number(l):
        b_str = ''
        for c in l:
            b_str += str(wires[c])
        return int(b_str, 2)

    #wires = wires_o.copy()
    #gates = gates_o.copy()
    #execute(wires, gates)

    #get_number(xs)
    x = get_number(xs)
    y = get_number(ys)
    z_exp = x & y
    #print(xs, get_number(xs))
    #print(ys, get_number(ys))
    #print(zs, get_number(zs), get_number(xs)&get_number(ys))

    pairs = []
    for k in range(len(gates)):
        for l in range(k+1, int(len(gates)/4)):
            pairs.append((k, l))
    #print(pairs)

    for k in range(len(pairs)):
        kp = pairs[k]
        for l in range(k+1, len(pairs)):
            lp = pairs[l]
            k1, k2 = kp
            l1, l2 = lp
            a = set([k1, k2, l1, l2])
            if len(a) < 4:
                continue
            wires = wires_o.copy()
            gates = gates_o.copy()
            if kp == (0, 5) and lp == (1,2):
                #pdb.set_trace()
                pass
            t = gates[k1*4+3]
            gates[k1*4+3] = gates[k2*4+3]
            gates[k2*4+3] = t
            t = gates[l1*4+3]
            gates[l1*4+3] = gates[l2*4+3]
            gates[l2*4+3] = t
            execute(wires, gates)


            zs = []
            for w in wires:
                if w.startswith('z'):
                    zs.append(w)
            zs.sort(reverse=True)
            z = get_number(zs)
            #print(z, zs)
            if z == z_exp:
                print(kp, lp)
                pass

            pass
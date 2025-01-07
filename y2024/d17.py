import time

from AoCutils.utils import print_complete


def run():
    print("2024, day 17")

    def program(program, regs):
        a, b, c = regs
        ip = 0
        output = []
        while ip < len(program):
            opcode = program[ip]
            operand = program[ip+1]

            if 0 <= operand <= 3:
                value = operand
            elif operand == 4:
                value = a
            elif operand == 5:
                value = b
            elif operand == 6:
                value = c

            if opcode == 0: # adv
                a = int(a / 2**value)
            elif opcode == 1:
                b = b ^ operand
            elif opcode == 2:
                b = value % 8
            elif opcode == 3: # jnz
                if a == 0:
                    pass
                else:
                    ip = operand
                    continue
            elif opcode == 4:
                b ^= c
            elif opcode == 5: # out
                output.append(value % 8)
            elif opcode == 6:
                sys.exit(0)
                pass
            elif opcode == 7: # cdv
                c = int(a / 2**value)

            ip += 2

        return output

    # Part 1
    time_0 = time.time()

    output = program([2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0], [48744869, 0, 0])

    print_complete(time_0, ','.join(map(str, output)))

    # Part 2
    time_0 = time.time()
    p_ref = [2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0]

    c = []
    i = 0
    A = 0
    # find number of digits
    while len(c) < len(p_ref):
        A = 2**i
        c = program(p_ref, [A, 0, 0])
        i += 1

    for k in range(A, 2*A, int(A/1000000)):
        a = k
        c = program(p_ref, [a, 0, 0])
        if c[12:] == p_ref[12:]:
            break
    for m in range(k, 2*k, int(k/10000000)):
        a = m
        c = program(p_ref, [a, 0, 0])
        if c[8:] == p_ref[8:]:
            break
    for k in range(m, 2*m, int(m/1000000000)):
        a = k
        c = program(p_ref, [a, 0, 0])
        if c[4:] == p_ref[4:]:
            break
    for m in range(k, 2*k):
        a = m
        c = program(p_ref, [a, 0, 0])
        if c == p_ref:
            break

    print_complete(time_0, a)
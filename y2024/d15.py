class Board:
    def __init__(self, data):
        self.pos = None
        self.data = []
        for y in range(len(data)):
            line = data[y]
            if line == '':
                break
            self.data.append(line)
            if '@' in line:
                self.pos = (line.index('@'), y)

    def step(self, d):
        if d == '^':
            y = self.pos[1]
            x = self.pos[0]
            l = 0
            n = 0
            while y-n > 0:
                if self.data[y-n][x] == '.':
                    l = 1
                    break
                elif self.data[y-n][x] in ['O', '@']:
                    n += 1
                else:
                    break
            # print(n, l)
            if l > 0:
                self.pos = (x, y-1)
                for k in range(n-1,-1,-1):
                    self.data[y-k-1] = self.data[y-k-1][:x] + self.data[y-k][x] + self.data[y-k-1][x+1:]
                    self.data[y-k] = self.data[y-k][:x] + '.' + self.data[y-k][x+1:]
        if d == 'v':
            y = self.pos[1]
            x = self.pos[0]
            l = 0
            n = 0
            while y+n < len(self.data):
                if self.data[y+n][x] == '.':
                    l = 1
                    break
                elif self.data[y+n][x] in ['O', '@']:
                    n += 1
                else:
                    break
            #print(n, l)
            if l > 0:
                self.pos = (x, y+1)
                for k in range(n-1, -1, -1):
                    self.data[y+k+1] = self.data[y+k+1][:x] + self.data[y+k][x] + self.data[y+k+1][x+1:]
                    self.data[y+k] = self.data[y+k][:x] + '.' + self.data[y+k][x+1:]
        if d == '<':
            y = self.pos[1]
            x = self.pos[0]
            l = 0
            n = 0
            while x-n > 0:
                if self.data[y][x-n] == '.':
                    l = 1
                    break
                elif self.data[y][x-n] in ['O', '@']:
                    n += 1
                else:
                    break
            #print(n, l)
            #print(self.pos)
            if l > 0:
                self.pos = (x-1, y)
                #print(x-n,',',x-n+1,x+1,',',x+n)
                self.data[y] = self.data[y][:x-n] + self.data[y][x-n+1:x+1] + '.' + self.data[y][x+1:]
        if d == '>':
            y = self.pos[1]
            x = self.pos[0]
            l = 0
            n = 0
            while x+n < len(self.data[0]):
                if self.data[y][x+n] == '.':
                    l = 1
                    break
                elif self.data[y][x+n] in ['O', '@']:
                    n += 1
                else:
                    break
            # print(n, l)
            if l > 0:
                self.pos = (x+1, y)
                self.data[y] = self.data[y][:x] + '.' + self.data[y][x:x+n] + self.data[y][x+n+1:]

    def print(self):
        for line in self.data:
            print(line)

    def boxsum(self):
        s = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if self.data[y][x] == 'O':
                    s += 100*y + x
        return s

    def count(self):
        c = 0
        for line in self.data:
            c += line.count('O')
        return c
    
def main():
    lines = [line.strip() for line in open("15.txt")]
    # lines = [line.strip() for line in open("15.example.txt")]

    b = Board(lines)
    b.print()
    print()
    cnt = b.count()
    c = 0
    start = False
    for line in lines:
        if line == '':
            start = True
        elif start:
            for m in line:
                c += 1
                #print(m, c)
                b.step(m)
                #b.print()
                if b.count() != cnt:
                    print('ERROR!', c)
                    break
                # if c > 10:
                #    break
            # break

    b.print()
    print(b.boxsum())

if __name__ == '__main__':
    main()

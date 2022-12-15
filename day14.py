
def parse_grid(input):
    grid = []
    for line in input.splitlines():
        positions = [[int(x) for x in pos.split(',')] for pos in line.split(" -> ")]
        n = len(positions)
        for i in range(1, n):
            a = positions[i-1]
            b = positions[i]
            rng = expand_rng(a, b)
            grid.extend(rng)
    return set(grid)

def expand_rng(a, b):
    x0, y0 = a
    x1, y1 = b
    if x0 == x1:
        dy = y1 - y0
        s = dy // abs(dy)
        return [(x0, y0+y) for y in range(0, dy+s, s)]
    elif y0 == y1:
        dx = x1 - x0
        s = dx // abs(dx)
        return [(x0+x, y0) for x in range(0, dx+s, s)]
    return None

class Grid():
    def __init__(self, input):
        self.grid = parse_grid(input)
        self.xmin = min([x[0] for x in self.grid])
        self.xmax = max([x[0] for x in self.grid])
        self.ymin = min([x[1] for x in self.grid])
        self.ymax = max([x[1] for x in self.grid])
        self.count = 0
        self.void_reached = False
        self.has_floor = False

    def add_floor(self, buffer = 10):
        for x in range(self.xmin-buffer, self.xmax+buffer):
            self.grid.add((x, self.ymax + 2))
        self.has_floor = True
        
    def drop_sand(self):
        x, y = (500, 0)
        while True:
            if self.has_floor:
                if (501, 1) in self.grid:
                    self.count += 1
                    self.grid.add((x, y))
                    break
            elif y == self.ymax:
                self.void_reached = True
                break
            y1 = y + 1
            if (x, y1) not in self.grid:
                y = y1
                continue
            else:
                if (x - 1, y1) not in self.grid:
                    x -= 1
                    y = y1
                    continue
                elif (x + 1, y1) not in self.grid:
                    x += 1
                    y = y1
                    continue
                else:
                    self.count += 1
                    self.grid.add((x, y))
                    return (x, y)
        return None


x = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
x = open('data/day14.txt').read()
g = Grid(x)
while True:
    g.drop_sand()
    if g.void_reached:
        break
print(g.count)

g = Grid(x)
g.add_floor(1000)
while True:
    v = g.drop_sand()
    if not v:
        break
print(g.count)

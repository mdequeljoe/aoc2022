

def shift_x(x, n=2, lim_x=6):
    coords = []
    for el in x:
        if n > 0 and el[0] + n >= lim_x:
            return x
        if n < 0 and el[0] + n <= lim_x:
            return x
        coords.append((el[0] + n, el[1]))
    return coords

def shift_y(x, n=3):
    return [(x[0], x[1] + n) for x in x]

def min_y(x):
    return min([x[1] for x in x])
def max_y(x):
    return max([x[1] for x in x])

class Grid():
    def __init__(self, shapes, stream):
        self.points = set([(x, 0) for x in range(7)])
        self.current_height = 0
        self.current_dir = 0
        self.y_offset = 3 + 1
        self.shapes = shapes
        self.current_shape = 0
        self.reset_height = []
        self.n_dropped = 0
        self.stream = list(stream)
    
    def movable(self, new_position):
        for k in new_position:
            if k in self.points:
                return False
        return True
    
    def update_height(self):
        self.current_height = max_y(self.points)

    def add_points(self, position):
        for coord in position:
            self.points.add(coord)

    def add_shape(self):
        dirs = []
        current_height = self.current_height
        current_shape = self.current_shape
        s = self.shapes[current_shape]
        s = shift_y(s, current_height + self.y_offset)
        self.current_shape = (self.current_shape + 1) % len(self.shapes)
        h = min_y(s)
        while True:
            direction = self.stream[self.current_dir]
            if self.current_dir == 0:
                self.reset_height.append([self.n_dropped, self.current_height])
            self.current_dir = (self.current_dir + 1) % len(self.stream)
            if direction == '<':
                s1 = shift_x(s, -1, -1)
            else:
                s1 = shift_x(s, 1, 7)
            m = self.movable(s1)
            if m:
                s = s1
                dirs.append(direction)

            s1 = shift_y(s, -1)
            m = self.movable(s1)
            if m:
                s = s1
            else:
                self.last_shape = s
                self.add_points(s)
                self.update_height()
                break
        self.n_dropped += 1
        if self.n_dropped % 5000 == 0:
            print('dropped:', self.n_dropped)

    def drop_shapes(self, n):
        for _ in range(n):
            self.add_shape()

    def drop_shapes2(self, n, count_after):
        for i in range(n):
            if i == count_after:
                h = self.current_height
            self.add_shape()
        return self.current_height - h
     

bar = [(x, 0) for x in range(4)]
plus = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
j = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
l = [(0, y) for y in range(4)]
square = [(0, 0), (1, 0), (0, 1), (1, 1)]

shapes = [shift_x(bar), shift_x(plus), shift_x(j), shift_x(l), shift_x(square)]
stream = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

g = Grid(shapes, stream)
g.add_shape()
assert g.last_shape == [(2, 1), (3, 1), (4, 1), (5, 1)]

g.add_shape()
assert g.last_shape == [(3, 2), (2, 3), (3, 3), (4, 3), (3, 4)]

g.add_shape()
assert g.last_shape ==  [(0, 4), (1, 4), (2, 4), (2, 5), (2, 6)]

stream = open('data/day17.txt').read()
g = Grid(shapes, stream)
g.drop_shapes(2022)
print(g.current_height)

# part two
# check cycles:
# g = Grid(shapes, stream)
# g.drop_shapes(len(stream) * 3)
# for i in range(1, len(g.reset_height)):
#     print('n:', g.reset_height[i][0], 'n diff:', g.reset_height[i][0] - g.reset_height[i - 1][0], 'h:', g.reset_height[i][1], 'h diff:', g.reset_height[i][1] - g.reset_height[i - 1][1])
# n: 1723 n diff: 1723 h: 2721 h diff: 2721
# n: 3448 n diff: 1725 h: 5430 h diff: 2709
# n: 5173 n diff: 1725 h: 8139 h diff: 2709
# n: 6898 n diff: 1725 h: 10848 h diff: 2709
# n: 8623 n diff: 1725 h: 13557 h diff: 2709


h = 0
n_drop = 1_000_000_000_000
h += 2721
n_rem = n_drop - 1723
m = n_rem // 1725  
h += m * 2709
rem = n_rem % 1725
g = Grid(shapes, stream)
h += g.drop_shapes2(1723 + rem, 1723)
print(h)


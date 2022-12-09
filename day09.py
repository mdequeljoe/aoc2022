
class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = []
    def current_pos(self):
        return (self.x, self.y)
    def points_visited(self):
        return self.visited
    def follow(self, x0, y0):
        dx = x0 - self.x
        dy = y0 - self.y
        d = (dx, dy)
        # follow to the right
        if dx >= 2 and dy == 0:
            self.x += 1
        # follow to the left
        elif dx <= -2 and dy == 0:
            self.x -= 1
        # follow up 
        elif dx == 0 and dy <= -2:
            self.y -= 1
        # follow down   
        elif dx == 0 and dy >= 2:  
            self.y += 1
        # up or down diagonally
        # follow to the upper right
        elif dx == 1 and dy <= -2:
            self.x += 1
            self.y -= 1
        # follow to the upper left
        elif dx <= -1 and dy <= -2:
            self.x -= 1
            self.y -= 1
        # follow to the lower right
        elif dx >= 1 and dy >= 2:
            self.x += 1
            self.y += 1
        # follow to the lower left
        elif dx <= -1 and dy >= 2:
            self.x -= 1
            self.y += 1
        # to the side diagonally
        # side right-up
        elif dx >= 2 and dy <= -1:
            self.x += 1
            self.y += -1
        # side right-down
        elif dx >= 2 and dy >= 1:
            self.x += 1
            self.y += 1
        # side left-up
        elif dx <= -2 and dy <= -1:
            self.x += -1
            self.y += -1
        # side left-down
        elif dx <= -2 and dy >=  1:
            self.x += -1
            self.y += 1
        self.visited.append((self.x, self.y))

class Cord:
    def __init__(self):
        self.head = Knot()
        self.tail = Knot()
    def move(self, direction, distance):
        moves = {'R': 1, 'L': -1, 'U': -1, 'D': 1}
        if direction in ['R', 'L']:
            for i in range(distance):
                self.head.x += moves[direction]
                self.head.visited.append((self.head.x, self.head.y))
                self.tail.follow(self.head.x, self.head.y)
        if direction in ['U', 'D']:
            for i in range(distance):
                self.head.y += moves[direction]
                self.head.visited.append((self.head.x, self.head.y))
                self.tail.follow(self.head.x, self.head.y)

def parse(x):
    x = [x.split(" ") for x in x.splitlines()]
    x = [(x[0], int(x[1])) for x in x]
    return x

x = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

x = open('data/day09.txt').read()
x = parse(x)
cord = Cord()
for line in x:
    cord.move(line[0], line[1])
v = set(cord.tail.points_visited())
print(len(v))

# part two
class MultiCord:
    def __init__(self, n):
        self.knots = [Knot() for i in range(n)]
    def move(self, direction, distance):
        moves = {'R': 1, 'L': -1, 'U': -1, 'D': 1}
        if direction in ['R', 'L']:
            for i in range(distance):
                self.knots[0].x += moves[direction]
                self.knots[0].visited.append((self.knots[0].x, self.knots[0].y))
                for k in range(1, len(self.knots)):
                    self.knots[k].follow(self.knots[k-1].x, self.knots[k-1].y)
        if direction in ['U', 'D']:
            for i in range(distance):
                self.knots[0].y += moves[direction]
                self.knots[0].visited.append((self.knots[0].x, self.knots[0].y))
                for k in range(1, len(self.knots)):
                    self.knots[k].follow(self.knots[k-1].x, self.knots[k-1].y)

                
x = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

x = open('data/day09.txt').read()
x = parse(x)
cord = MultiCord(10)
for line in x:
    cord.move(line[0], line[1])
v = set(cord.knots[-1].points_visited())
print(len(v))
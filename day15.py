import re

def parse(input):
    res = []
    for line in input.splitlines():
        line = re.sub("[^0-9+|=|-]", "", line).split('=')
        x0, y0, x1, y1 = [int(x) for x in line[1:]]
        res.append([(x0, y0), (x1, y1)])
    return res

def manhattan_dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

# manhattan area upper right hand boundary
def ma_boundary(x0, y0, x1, y1):
    d = manhattan_dist(x0, y0, x1, y1)
    area = {}
    h = d
    for r in range(d + 1):
        area[x0 + r] = y0 - h
        h -= 1
    return area

class Sensor():
    def __init__(self, xs, ys, xb, yb):
        self.xs = xs
        self.ys = ys
        self.xb = xb
        self.yb = yb
        self.d = manhattan_dist(xs, ys, xb, yb)
        self.area = ma_boundary(xs, ys, xb, yb)
        self.y_area = {v:k for k, v in self.area.items()}
        self.ymin = ys - self.d
        self.ymax = ys + self.d

class Grid():
    def __init__(self, input):
        self.sensors = {}
        self.beacons = set()
        for sensor, beacon in parse(input):
            xs, ys = sensor
            xb, yb = beacon
            self.beacons.add((xb, yb))
            self.sensors[(xs, ys)]= Sensor(xs, ys, xb, yb)
    def scan_line(self, y):
        seen = set()
        for key, sensor in self.sensors.items():
            x0 = sensor.xs
            y0 = sensor.ys
            if y < sensor.ymin or y > sensor.ymax:
                continue
            for xs, ys in sensor.area.items():
                if (xs, y) in self.beacons:
                    continue
                d = abs(ys - y0)
                if y0 + d >= y >= ys:
                    seen.add((xs, y))
                    seen.add((x0 - (xs - x0), y))
                else:
                    break
        return seen


input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

# g = Grid(input)
# ans = g.scan_line(10)

input = open('data/day15.txt').read()
g = Grid(input)
ans = g.scan_line(2000000)
print(len(ans))

# part two

# if in lower half of area get corresponding y in upper half 
def mirror_y(ys, y):
    return ys - (y - ys)

def find_gap(rng, x_min = float('-inf'), x_max = float('inf')):
    rng = sorted(rng)
    b = rng[0][1]
    for i in range(1, len(rng)):
        x0, x1 = rng[i]
        if x1 > x_max:
            break
        d = x0 - b
        if d > 1:
            return b + 1
        elif x1 > b:
            b = x1
    return None

input = open('data/day15.txt').read()
g = Grid(input)
for n in range(4000000):
    if n % 100_000 == 0:
        print(n)
    x_ranges = []
    for key, sensor in g.sensors.items():
        if n < sensor.ymin or n > sensor.ymax:
            continue
        x0 = sensor.xs
        if n in sensor.y_area.keys():
            x_rng = (x0 - (sensor.y_area[n] - x0), sensor.y_area[n])
            x_ranges.append(x_rng)
        elif (m:= mirror_y(sensor.ys, n)) in sensor.y_area.keys():
            x_rng = (x0 - (sensor.y_area[m] - x0), sensor.y_area[m])
            x_ranges.append(x_rng)
    gap = find_gap(x_ranges)
    if gap is not None:
        print('(x, y) =', (gap, n))
        print('tuning frequency = ', gap * 4_000_000 + n)
        break
    

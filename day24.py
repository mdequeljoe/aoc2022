
def parse(input):
    return [[list(x) for x in line] for line in input.splitlines()]

def parse(input):
    lines = input.splitlines()
    coords = []
    nr = len(lines)
    nk = len(lines[0])
    start = (1, 0)
    end = (nk - 2, nr - 1)
    lim_x = (0, nk - 1)
    lim_y = (0, nr - 1)
    for i in range(nr):
        for j in range(nk):
            if lines[i][j] in ['>', '<', '^', 'v']:
                coords.append((j, i, lines[i][j]))
    return start, end, lim_x, lim_y, coords

def move(coords, lx, ly):
    new_coords = []
    for x, y, d in coords:
        if d == '>':
            x += 1
            if x == lx[1]:
                x = lx[0] + 1
        elif d == '<':
            x -= 1
            if x == lx[0]:
                x = lx[1] - 1
        elif d == '^':
            y -= 1
            if y == ly[0]:
                y = ly[1] - 1
        elif d == 'v':
            y += 1
            if y == ly[1]:
                y = ly[0] + 1
        new_coords.append((x, y, d))
    return new_coords

def mdist(current, end):
    x0, y0 = current
    x1, y1 = end
    return abs(x1 - x0) + abs(y1 - y0)

def possible_steps(pos, coords, lx, ly, target):
    x, y = pos
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    steps = []
    for dx, dy in directions:
        x1 = x + dx
        y1 = y + dy
        if (x1, y1) == target:
            return [target]
        if (x1, y1) in coords:
            continue
        if lx[0] < x1 < lx[1] and ly[0] < y1 < ly[1]:
            steps.append((x1, y1))
    return steps

def h(coords):
    return "_".join(['{x=' + str(x) + 'y=' + str(y) + "}" for x, y in coords])

def xy(k):
    return set((x,y) for x,y,d in k)

def all_states(coords, lx, ly):
    s = []
    s.append(coords)
    while True:
        coords = move(coords, lx, ly)
        if coords in s:
            break
        s.append(coords)
    return s

def get_coord_data(coords, start, lx, ly):
    s = all_states(coords, lx, ly)
    states = {}
    starts = []
    key = {}
    n = len(s)
    for i in range(n):
        coords = xy(s[i])
        key[h(coords)] = s[i]
        states[h(coords)] = xy(s[(i + 1) % n])
        starts.append((i, start, coords))
    return starts, states, key

def min_path(start, end, lx, ly, coords):
    paths, states, key = get_coord_data(coords, start, lx, ly)
    nkeys = len(key)
    seen = set()
    m = float('inf')
    while True:
        if len(paths) == 0:
            break
        n, pos, coords = paths.pop(0)
        if (n % len(states), pos) in seen:
            continue
        seen.add((n % len(states), pos))
        m1 = mdist(pos, end)
        if m1 < m:
            print(m1)
            m = m1
        new_coords = states[h(coords)]
        steps = possible_steps(pos, new_coords, lx, ly, end)
        for s in steps:
            if s == end:
                return n + 1, key[h(new_coords)]
            paths.append((n + 1, s, new_coords))
        if n <= nkeys:
            paths.sort()
    return None, None

input = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""
input = open('data/day24.txt').read()
start, end, lx, ly, coords = parse(input)
m, k = min_path(start, end, lx, ly, coords)
m1, k1 = min_path(end, start, lx, ly, k)
m2, k2 = min_path(start, end, lx, ly, k1)
print(m)
print(m + m2 + m1)

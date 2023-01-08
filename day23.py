from collections import deque

def parse(input):
    lines = input.splitlines()
    coords = set()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                coords.add((j, i))
    return coords

def get_adj(x, y):
    return {
        'N': (x, y - 1),
        'S': (x, y + 1),
        'W': (x - 1, y),
        'E': (x + 1, y),
        'NW': (x - 1, y - 1),
        'SW': (x - 1, y + 1),
        'SE': (x + 1, y + 1),
        'NE': (x + 1, y - 1)
    }

def play_rounds(input, n_rounds):
    coords = parse(input)
    directions = deque([
        [['N', 'NE', 'NW'], 'N'],
        [['S', 'SE', 'SW'], 'S'],
        [['W', 'NW', 'SW'], 'W'],
        [['E', 'NE', 'SE'], 'E']
    ])
    for round in range(n_rounds):
        k = coords.copy()
        prop = []
        dest_coords = []
        for x, y in coords:
            a = get_adj(x, y)
            if not any(el in coords for el in a.values()):
                continue
            for dirs, dest in directions:
                if all(a[d] not in coords for d in dirs):
                    prop.append(a[dest])
                    dest_coords.append((x, y))
                    break
        for i in range(len(prop)):
            cnt = prop.count(prop[i])
            if cnt == 1:
                coords.remove(dest_coords[i])
                coords.add(prop[i])
        if k == coords:
            return(round + 1)
        directions.rotate(-1)
    return coords

def empty_tiles(coords):
    min_x = min(x for x, y in coords)
    max_x = max(x for x, y in coords)
    min_y = min(y for x, y in coords)
    max_y = max(y for x, y in coords)
    return set((x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)) - coords

input = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""
input = open('data/day23.txt').read()
p = play_rounds(input, 10)
print(len(empty_tiles(p)))

p = play_rounds(input, 1000)
print(p)
from string import ascii_lowercase 
from queue import PriorityQueue

def parse(input):
    return[list(lines) for lines in input.splitlines()]

def get_adjacent(grid, coord):
    row, col = coord
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    adj = []
    nr, nk = len(grid), len(grid[0])
    for dir in directions:
        dr = dir[0] + row
        dk = dir[1] + col
        if 0 <= dr < nr and 0 <= dk < nk:
            adj.append((dr, dk))  
    return adj

def get_val(grid, coord):
    row, col = coord
    return grid[row][col]

def get_height(letters, val):
    if val == 'E':
        return get_height(letters, 'z')
    if val == 'S':
        return get_height(letters, 'a')
    return letters[val]

def get_start_pos(grid, val="S"):
    pos = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == val:
                pos.append((i, j))
    return pos

def run_grid(grid, start_pos=(0,0)):
    letters = {v:c for c, v in enumerate(ascii_lowercase)}
    q = PriorityQueue()
    q.put((0, 0, start_pos))
    seen = []
    while True:
        if q.empty():
            break
        height, steps, pos = q.get()
        if pos in seen:
            continue
        seen.append(pos)
        adj_coords = get_adjacent(grid, pos)
        for coord in adj_coords:
            if coord in seen:
                continue
            val = get_val(grid, coord)
            h = get_height(letters, val)*-1
            if h < height - 1:
                continue
            if val == "E":
                return steps + 1
            q.put((h, steps + 1, coord))
    return None

x = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
x = parse(x)
# print(run_grid(x))

x = open('data/day12.txt').read()
x = parse(x)
pos = get_start_pos(x)
print(run_grid(x, pos[0]))

# part two
coords = get_start_pos(x, "a")
n = len(coords)
ans = []
for i in range(n):
    res = run_grid(x, coords[i])
    if res:
        ans.append(res)
print(min(ans))




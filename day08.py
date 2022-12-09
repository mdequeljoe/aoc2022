
def parse_grid(grid):
    grid = [list(x) for x in grid.splitlines()]
    grid = [[int(x) for x in tree] for tree in grid]
    return grid

def get_ranges(grid, r, k, rows, cols):
    return {
        'left': [grid[r][i] for i in range(k)],
        'right': [grid[r][i] for i in range(k+1, cols)],
        'up': [grid[i][k] for i in range(r)],
        'down': [grid[i][k] for i in range(r+1, rows)]
    }

def is_visible(grid, r, k, rows, cols):
    val = grid[r][k]
    rng = get_ranges(grid, r, k, rows, cols)
    if max(rng["left"]) < val:
        return True
    if max(rng["right"]) < val:
        return True 
    if max(rng["up"]) < val:
        return True
    if max(rng["down"]) < val:
        return True
    return False

def count_visible(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = (2 * rows) + (2 * cols) - 4
    for r in range(1, rows-1):
        for k in range(1, cols-1):
            if is_visible(grid, r, k, rows, cols):
                count += 1
    return count

grid = """30373
25512
65332
33549
35390"""
grid = open('data/day08.txt').read()

x = parse_grid(grid)
print(count_visible(x))

# part 2
def get_score(val, values):
    score = 0
    for v in values:
        score += 1
        if v >= val:
            break
    return score

def get_view(grid, r, k, rows, cols):
    val = grid[r][k]
    rng = get_ranges(grid, r, k, rows, cols)
    rng["left"].reverse()
    rng["up"].reverse()
    score = get_score(val, rng["left"])
    score *= get_score(val, rng["right"]) 
    score *= get_score(val, rng["up"]) 
    score *= get_score(val, rng["down"])
    return score

def max_view(grid):
    rows = len(grid)
    cols = len(grid[0])
    score = 0
    for r in range(1, rows-1):
        for k in range(1, cols-1):
            view = get_view(grid, r, k, rows, cols)
            if view > score:
                score = view
    return score

print(max_view(x))

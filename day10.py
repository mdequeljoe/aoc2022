
def parse(input):
    res = []
    for line in input.splitlines():
        ins, *num = line.split(" ")
        if len(num) == 1:
            res.append([ins, int(num[0])])
        else:
            res.append([ins])
    return res

def run_cycles(input, n):
    cycle = {i+1: None for i in range(n)}
    cycle[1] = 1
    for k in cycle.keys():
        if len(input) == 0:
            break
        ins = input.pop(0)
        if cycle[k] is not None:
            x = cycle[k]
        else:
            cycle[k] = x
        if ins[0] == "noop":
            pass
        elif ins[0] == "addx":
            cycle[k + 2] = x + ins[1]
            input[0:0] = [["noop"]]
    return cycle

input = """noop
addx 3
addx -5"""
input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
input = open("data/day10.txt").read()
input = parse(input)
k = run_cycles(input, 240)
targets = [20, 60, 100, 140, 180, 220]
print(
    sum([k[t] * t for t in targets])
)

# part two 
def gen_crt(w=40, h=6):
    return [['.' for w in range(w)] for h in range(h)]

def get_sprite(row, pos):
    return [(row, pos - 1), (row, pos), (row, pos + 1)]

def draw_image(input):
    crt = gen_crt()
    row = col = 0
    n = 240
    k = run_cycles(input, 240)
    for i in range(1, n + 1): 
        pos = k[i]
        row = (i - 1) // 40
        sprite = get_sprite(row, pos)
        if col in [s[1] for s in sprite]:
            crt[row][col] = '#'
        col = (col + 1) % 40
    return crt

def cat_image(img):
    img = [[" " if x == "." else x for x in row] for row in img]  
    return "\n".join(["".join(row) for row in img])

input = open("data/day10.txt").read()
input = parse(input)
img = draw_image(input)
print(cat_image(img))
#RKAZAJBR
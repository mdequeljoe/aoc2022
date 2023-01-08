from sympy.parsing.sympy_parser import parse_expr
from sympy.solvers import solve
from sympy import Symbol

def parse(input, use_floor_division=True):
    m = {}
    for line in input.splitlines():
        l = line.split(' ')
        monkey = l[0].replace(":", "")
        if l[1].isdigit():
            m[monkey] = int(l[1])
        else:
            if use_floor_division and l[2] == "/":
                l[2] = "//"
            m[monkey] = l[1:4]
    return m

def is_int(x):
    return type(x) == int
def calc_ready(l):
    return is_int(l[0]) and is_int(l[2])
def do_calc(l):
    res = eval(" ".join([str(x) for x in l]))
    return res

def run_process(d):
    while True:
        for m in d.keys():
            if not is_int(d[m]):
                a = d[m][0]
                b = d[m][2]
                if not is_int(a):
                    if is_int(d[a]):
                        d[m][0] = d[a]
                if not is_int(b):
                    if is_int(d[b]):
                        d[m][2] = d[b]
                if calc_ready(d[m]):
                    d[m] = do_calc(d[m])
        if is_int(d['root']):
            break
    return d
                
input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

input = open('data/day21.txt').read()
d = parse(input)
x = run_process(d)
print(x['root'])

def get_calculations(d, m):
    if is_int(d[m]):
        return d[m]
    if m == 'humn':
        return d[m]
    d[m][0] = [get_calculations(d, d[m][0])]
    d[m][2] = [get_calculations(d, d[m][2])]
    return d[m]

def str_calc(calc):
    res = []
    for l in calc:
        if isinstance(l, list):
            res += '('
            res += str_calc(l)
            res += ')'
        else:
            res += str(l)
    return res

# part two, solve for x
input = open('data/day21.txt').read()
d = parse(input, False)
d['humn'] = 'x'
d['root'][1] = '-'
g = get_calculations(d, 'root')
sg = str_calc(g)
sg = "".join(sg)
e = parse_expr(sg)
x = Symbol('x')
print(solve(e))


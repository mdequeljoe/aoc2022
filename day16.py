from itertools import permutations

def parse(input):
    d = {}
    for line in input.splitlines():
        l = line.split(" ")
        valve = l[1]
        rate = l[4][:-1].split("=")[1]
        connected_valves = [x.replace(',', '') for x in l[9:]]
        d[valve] = {'rate':int(rate), 'connected':connected_valves}
    return d

def min_time(valves, current_valve, target_valve):
    qq = [(current_valve, 0, [])]
    min_t = float('inf')
    while qq:
        v, t, path = qq.pop(0)
        if v == target_valve:
            return t
        if v in path:
            continue
        path.append(v)
        for c in valves[v]['connected']:
            if c in path:
                continue
            p = path[:]
            p.append(v)
            qq.append((c, t + 1, p))
    return None

def get_min_times(valves):
    times = {}
    for v in valves.keys():
        print('getting min times for :', v)
        t = {}
        for nv in valves.keys():
            if v != nv:
                if nv in valves[v]['connected']:
                    t[nv] = 1
                elif nv in times.keys():
                    t[nv] = times[nv][v]
                else:
                    t[nv] = min_time(valves, v, nv)
        times[v] = t
    return times

# def expand(x):
#     n = len(x)
#     if n == 1:
#         return x
#     l = []
#     for el in x:
#         rem = [v for v in x if v != el]
#         for k in expand(rem):
#             if isinstance(k, list):
#                 l.append([el] + k)
#             else:
#                 l.append([el] + [k])
#     return l        

def get_all_paths(valves, n, root=[]):
    k = [k for k in valves.keys() if valves[k]['rate'] != 0]
    if len(k) == 1:
        return [root + k]
    paths = permutations(k, n)
    return [root + list(p) for p in paths]

def open_valves(valves, path, min_times, time_limit=30):
    stock = 0
    flows = []
    n = len(path)
    minute = 0
    for i in range(1, n):
        current_valve, target_valve = path[i - 1], path[i]
        steps = min_times[current_valve][target_valve]
        # + 1 since it takes one minute to open the value after stepping
        for _ in range(steps + 1):
            stock += sum(flows)
            minute += 1
            if minute == time_limit:
                return stock
        # print(current_valve, target_valve, 'steps=', steps, 'opened at minute=', minute)
        flows.append(valves[target_valve]['rate'])
    for _ in range(minute, time_limit):
        stock += sum(flows)
    return stock

input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
valves = parse(input)


input = open('data/day16.txt').read()
valves = parse(input)
kpath = []
t = get_min_times(valves)
paths = get_all_paths(valves, 5, ['AA'])
target_valves = [k for k,v in valves.items() if valves[k]['rate'] != 0]
while True:
    scores = []
    for p in paths:
        s = open_valves(valves, p, t)
        scores.append((s, p))
    scores = sorted(scores)[-1]
    kpath = scores[1]
    if len(kpath) == len(target_valves) + 1:
        break
    p = {k:v for k,v in valves.items() if k not in kpath}
    paths = get_all_paths(p, min(5, len(p)), kpath)
print(scores)

# part two
# 7, 8 or 6, 9
rem_valves = target_valves
p1 = permutations([k for k in valves.keys() if valves[k]['rate'] != 0], 6)
score = 0
sp = []
cnt = 0
for p in p1:
    s = open_valves(valves, ['AA'] + list(p), t, 26)
    cnt +=1
    if s > score:
        print(s, p, cnt)
        score = s
        sp.append((s, p))
pairs = []
for s, path in sp:
    p2 = permutations([k for k in valves.keys() if k not in path and valves[k]['rate'] != 0], 9)
    score2 = 0
    cnt = 0
    for p in p2:
        s2 = open_valves(valves, ['AA'] + list(p), t, 26)
        cnt +=1
        if s2 > score2:
            print(s + s2, s, path, s2, p, cnt)
            score2 = s2
            pairs.append((s2 + s, s, path, s2, p))
pairs.sort(reverse=True)
print(pairs[0])

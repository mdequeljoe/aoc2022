from copy import deepcopy
def parse(x):
    res = []
    for pairs in x.split("\n\n"):
        pair = pairs.split("\n")
        p0 = eval(pair[0])
        p1 = eval(pair[1])
        res.append([p0, p1])
    return res

def is_int(x):
    return isinstance(x, int)
def is_list(x):
    return isinstance(x, list)

def is_sorted(p0, p1):
    while True:
        n0 = len(p0)
        n1 = len(p1)
        if n0 == 0:
            return True
        if n1 == 0 and n0 > 0:
            return False
        a = p0.pop(0)
        b = p1.pop(0)
        if is_int(a) and is_int(b):
            if a > b:
                return False
            elif a == b:
                continue
            else:
                return True
        elif is_list(a) and is_list(b):
            if len(a) == 0 and len(b) == 0:
                continue
            else:
                return is_sorted(a, b)	
        elif is_list(a) and is_int(b):
            return is_sorted(a, [b])
        elif is_int(a) and is_list(b):
            return is_sorted([a], b)

def count_sorted(input):
    x = parse(input)
    ans = []
    for pair in x:
        res = is_sorted(pair[0], pair[1])
        ans.append(res)
    id = [i + 1 for i in range(len(ans)) if ans[i]] 
    return sum(id)

input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
# print(count_sorted(input))

input = open('data/day13.txt').read()
print(count_sorted(input))
    
# part two
input = open('data/day13.txt').read()
x = parse(input)
l = []
for pair in x:
    l.append(pair[0])
    l.append(pair[1])
l.insert(0, [[2]])
l.insert(1, [[6]])
l = sorted(l, key = len)

def pair_sort(x):
    i = 0
    n = len(x)
    all_sorted = True
    while True:
        if i == n - 1:
            if all_sorted:
                break
            else:
                i = 0
                all_sorted = True
                continue
        j = i + 1
        a = deepcopy(x[i])
        b = deepcopy(x[j])
        if not is_sorted(a, b):
            all_sorted = False
            x.insert(i, x.pop(j))
        i += 1
    return x

ans = pair_sort(l)
n = len(ans)
keys = [i + 1 for i in range(n) if ans[i] == [[2]] or ans[i] == [[6]]]
print(keys[0] * keys[1])
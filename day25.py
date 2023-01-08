def decode(num):
    num = list(num)
    n = len(num)
    p = 0
    for i in range(n-1, -1, -1):
        if not num[i].isdigit():
            if num[i] == '-':
                num[i] = -1
            elif num[i] == '=':
                num[i] = -2
        num[i] = int(num[i]) * (5 ** p)
        p += 1
    print(num)
    return sum(num)

def recode(num):
    s = 0
    i = 0
    while True:
        s += 5 ** i * 2
        if s >= num:
            break
        i += 1
    n = i + 1
    id = []
    for i in range(n-1, -1, -1):
        s = 5 ** i
        rng = [1, 2, 0, -1, -2]
        d = [abs(num - s * r) for r in rng]
        m = min(d)
        v = rng[d.index(m)] 
        id.append(v)
        num = num - v * s
    for i in range(len(id)):
        if id[i] == -2:
            id[i] = '='
        elif id[i] == -1:
            id[i] = '-'
        else:
            id[i] = str(id[i])
    return ''.join(id)

input = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

input = open('data/day25.txt').read()
s = 0
for num in input.splitlines():
    s += decode(num)
print(recode(s))

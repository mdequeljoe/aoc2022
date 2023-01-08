from collections import deque

def mix(x, decryption_key=1, times=10):
    key = [(i, v * decryption_key) for i, v in enumerate(x)]
    d = deque(key)
    for _ in range(times):
        for el in key:
            id = d.index(el)
            d.rotate(-id)
            d.popleft()
            d.rotate(-el[1])
            d.appendleft(el) 
    return [x[1] for x in d]

def decrypt(m):
    v = m.index(0)
    n = len(m)
    return sum([m[(v + offset) % n] for offset in [1000, 2000, 3000]])

x = open('data/day20.txt').read()
x = [int(x) for x in x.splitlines()]

m = mix(x, 1, 1)
print(decrypt(m))

m = mix(x, 811589153, 10)
print(decrypt(m))

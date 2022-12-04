
def expand_range(rng):
    start, end = rng.split('-')
    return range(int(start), int(end) + 1)

def in_range(x, rng, FUNC=all):
  return FUNC(x in rng for x in x)
  
x = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
x = open('data/day04.txt').read()
x = [[expand_range(x) for x in x.split(',')] for x in x.splitlines()]

partial_overlaps = overlaps = 0
for el in x:
    r1, r2 = el
    if in_range(r1, r2) or in_range(r2, r1):
        overlaps += 1
    if in_range(r1, r2, any) or in_range(r2, r1, any):
        partial_overlaps += 1
print(overlaps)
print(partial_overlaps)

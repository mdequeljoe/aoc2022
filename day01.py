x = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
x = open('data/day01.txt').read()
x = [x.split('\n') for x in x.split('\n\n')]
x = [[int(y) for y in elf] for elf in x]
ans = [sum(elf) for elf in x]
print(max(ans))
ans.sort()
print(sum(ans[-3:]))
x = """A Y
B X
C Z"""
x = open('data/day02.txt').read()
x = [x.split(' ') for x in x.splitlines()]

def convert_hand(v):
    if v in ['A', 'X', 'R']:
        return(('R', 1))
    if v in ['B', 'Y', 'P']:
        return(('P', 2))  
    return(('S', 3))

def rps(p1, p2):
    if p1[0] == p2[0]:
        return(3 + p2[1])
    if (p1[0], p2[0]) in [('R', 'S'), ('P', 'R'), ('S', 'P')]:
        return(p2[1])
    return(6 + p2[1])
    
score = 0
for round in x:
    p1 = convert_hand(round[0])
    p2 = convert_hand(round[1])
    score += rps(p1, p2)
print(score)

# part 2
winners = {'R': 'P', 'P':'S', 'S':'R'}
losers = {'R': 'S', 'P':'R', 'S':'P'}
score = 0
for round in x:
    p1 = convert_hand(round[0])
    ins = round[1]
    if ins == 'Y':
        p2 = p1
    elif ins == 'X':
        p2 = convert_hand(losers[p1[0]])
    else:
        p2 = convert_hand(winners[p1[0]])
    score += rps(p1, p2)
print(score)
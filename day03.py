import string
x = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
x = open('data/day03.txt').read()
x = [list(x) for x in x.splitlines()]

letters = string.ascii_lowercase

def get_priority(letter):
    val = letters.index(letter.lower()) + 1
    if letter.isupper():
        val += 26
    return val
  
score = 0
for el in x:
    n = len(el) // 2
    c1, c2 = el[:n], el[n:]
    common_letter = [v for v in c1 if v in c2][0]
    score += get_priority(common_letter)
print(score)

# part 2
score = 0
groups = range(0, len(x), 3)
for group in groups:
  g1, g2, g3 = x[group:group+3]
  badge = [v for v in g1 if v in g2 and v in g3][0]
  score += get_priority(badge)
print(score)

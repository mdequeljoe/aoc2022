import re
import copy

def parse_input(input):
  input = [re.sub('\[|\]', ' ', line) for line in input.splitlines()]
  input = [list(x) for x in input]
  stacks = {}
  num = input.pop()
  for i in range(len(num)):
      if num[i] == " ":
          continue
      v = int(num[i])
      stacks[v] = []
      for j in range(len(input)):
          if input[j][i] == " ":
              continue
          stacks[v].insert(0, input[j][i])
  return stacks

def parse_instructions(ins):
  ins = [x.split(' ') for x in ins.splitlines()]
  return [[int(x[1]), int(x[3]), int(x[5])] for x in ins]

def move_stacks(input, ins, order="forward"):
  stacks = copy.deepcopy(input)
  for line in ins:
    n, st, new_st = line
    v = [stacks[st].pop() for _ in range(n)]
    if order == "reverse":
      v.reverse()
    stacks[new_st].extend(v)
  return stacks

def stack_str(stacks):
  return "".join([v.pop() for k, v in stacks.items()])

input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """
ins = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
#input, ins = parse_input(input), parse_instructions(ins)

input = open('data/day05.txt').read().split("\n\n")
input, ins = parse_input(input[0]), parse_instructions(input[1])

ans = move_stacks(input, ins)
print(stack_str(ans))

# part two
ans = move_stacks(input, ins, "reverse")
print(stack_str(ans))

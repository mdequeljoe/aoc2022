
def find_signal(x, type='marker'):
  rng = 14
  if type == 'marker':
    rng = 4
  for i in range(rng, len(x)):
    v = x[i-rng:i]
    n = len(v)
    is_valid = True
    while True:
      el = v.pop()
      if el in v:
        is_valid = False
        break
      if len(v) == 0:
        break
    if is_valid:
      return i
  return -1

assert find_signal(list("mjqjpqmgbljsphdztnvjfqwrcgsmlb")) == 7
assert find_signal(list("nppdvjthqldpwncqszvftbrmjlhg")) == 6
assert find_signal(list("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")) == 10
assert find_signal(list("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")) == 11

x = open('data/day06.txt').read()
print(find_signal(list(x)))

# part two
assert find_signal(list("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), "msg") == 19
print(find_signal(list(x), 'msg'))

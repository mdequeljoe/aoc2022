import math  
def parse(x):
    monkeys = []
    x = [x.split(" ") for x in x.splitlines()]
    for i in range(len(x)):
        line = x[i]
        if line[0] == "Monkey":
            items = x[i + 1][4:]
            m = {
                "id": int(line[1][:-1]),
                "items_inspected": 0,
                "items": [int(item.replace(',', '')) for item in items],
                "operation": " ".join(x[i + 2][5:]),
                "test_divisible": int(x[i + 3][5]),
                "pass": int(x[i + 4][-1]),
                "fail": int(x[i + 5][-1])
            }
            monkeys.append(m)
    return monkeys

def eval_operation(op, old):
    return eval(op, {'old': old})

def play(monkeys, reduce_worry=True):
    if not reduce_worry:
        mod = math.prod([m['test_divisible'] for m in monkeys])
    for m in monkeys:
        while len(m['items']) > 0:
            item = m['items'].pop(0)
            m['items_inspected'] += 1
            new_item = eval_operation(m['operation'], item)
            if reduce_worry:
                new_item = new_item // 3
            else:
                new_item = new_item % mod
            md = new_item % m['test_divisible']
            if md == 0:
                monkeys[m['pass']]['items'].append(new_item)
            else:
                monkeys[m['fail']]['items'].append(new_item)
    return monkeys

x = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    
x = open('data/day11.txt').read()
x = parse(x)
for _ in range(20):
    play(x)
ans = [m['items_inspected'] for m in x]
ans.sort()
print(ans[-2] * ans[-1])
    
x = open('data/day11.txt').read()
x = parse(x)
for _ in range(10_000):
    play(x, False)
ans = [m['items_inspected'] for m in x]
ans.sort()
print(ans[-2] * ans[-1])

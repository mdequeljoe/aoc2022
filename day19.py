from queue import PriorityQueue

def h(t, stock, robots):
    return (tuple(stock.values()), tuple(robots.values()))

def pack(x):
    return tuple([v for v in x.values()])
def unpack(x):
    return {k:v for k, v in zip(['ore', 'clay', 'obsidian', 'geode'], x)}

class Blueprint():
    def __init__(self, input):
        x = input.split(" ")
        self.costs = {}
        self.costs['ore'] = [('ore', int(x[6]))]
        self.costs['clay'] = [('ore', int(x[12]))]
        self.costs['obsidian'] = [('ore', int(x[18])), ('clay', int(x[21]))]
        self.costs['geode'] = [('ore', int(x[27])), ('obsidian', int(x[30]))]
        self.robots = {'ore':1, 'clay':0, 'obsidian':0, 'geode':0 }
        self.stock = {'ore':0, 'clay':0, 'obsidian':0, 'geode':0}
        self.last_state = []

    def can_make(self, resource, stock, costs):
        for cost_resource, amt in costs[resource]:
            if stock[cost_resource] < amt:
                return False
        return True

    def possible_moves(self, stock, costs):
        if self.can_make('geode', stock, costs):
            return ['geode']
        if self.can_make('obsidian', stock, costs):
            return ['obsidian']
        moves = []
        for resource in costs.keys():
            if self.can_make(resource, stock, costs):
                moves.append(resource)
        return moves

    def get_resource(self, resource, stock, costs, robots):
        for cost_resource, amt in costs[resource]:
            stock[cost_resource] -= amt
        robots[resource] += 1
        return stock, robots

    def update_stock(self, stock, robots):
        for k, v in robots.items():
            stock[k] += v
        return stock

    def mine(self, time=24):
        states = PriorityQueue()
        states.put(( 0, 1, pack(self.robots), pack(self.stock)))
        geode_max = 0
        seen = set()
        while True:
            if states.empty():
                break
            gr, t, robots, stock = states.get()
            stock = unpack(stock)
            robots = unpack(robots)
            if t > time:
                if stock['geode'] > geode_max: 
                    geode_max = stock['geode']
                    print('geode=', geode_max)
                continue

            # estimate upper-bound of potential geodes
            # stock + (time - t) * (robots * 3) < geode_max then breal
            if stock['geode'] > 1:
                if stock['geode'] + (time + 1 - t) * robots['geode'] * 3 <= geode_max:
                    continue

            if h(t, stock, robots) in seen:
                continue
            seen.add(h(t, stock, robots))
            moves = self.possible_moves(stock, self.costs)
            if moves != ['geode'] or moves != ['obsidian']:
                s = stock.copy()
                r = robots.copy()
                s = self.update_stock(s, r)
                if h(t + 1, s, r) not in seen:
                    states.put((-s['geode'] + -r['geode'] * (time -t), t+1,  pack(r), pack(s)))

            for m in moves:
                s = stock.copy()
                r = robots.copy()
                s, r = self.get_resource(m, s, self.costs, r)
                s = self.update_stock(s, robots)
                if h(t + 1, s, r) not in seen:
                    states.put((-s['geode'] + -r['geode'] * (time -t),  t+1, pack(r), pack(s)))
                
        return geode_max

input = open('data/day19.txt').read().splitlines()
n = len(input)
mg = 0
s = 0
for i in range(n):
    b = Blueprint(input[i])
    g = b.mine()
    print(g)
    mg += g * (i + 1)
    s += g
print(s)
print(mg)

input = open('data/day19.txt').read().splitlines()
b = Blueprint(input[0])
g = b.mine(32)
print(g)

b = Blueprint(input[1])
g = b.mine(32)
print(g)

b = Blueprint(input[2])
g = b.mine(32)
print(g)


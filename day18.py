
def parse(input):
    return [
        tuple(int(x) for x in line.split(",")) for line in input.splitlines()
    ]

class Cube():
    def __init__(self, coords):
        self.coords = coords
        self.connected = set()
        self.internal = set()

def is_adjacent(x1, y1, z1, x2, y2, z2):
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1

def surrounding_cubes(x, y, z):
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1)
    ]

def in_range(v, lim):
    return all(
        lim[i][0] <= v[i] <= lim[i][1] for i in range(len(v))
    )

def air_pocket(coord, cube_coords, lims):
    x, y, z = coord
    adj = surrounding_cubes(x, y, z)
    cubes = [cube for cube in adj if cube in cube_coords]
    if len(cubes) == 6:
        return coord, adj
    elif len(cubes) == 0:
        return coord, None
    seen = set(cubes)
    qq = [cube for cube in adj if cube not in seen and in_range(cube, lims)]
    if len(qq) == 0:
        return coord, None
    air = set()
    while qq:
        c = qq.pop()
        if not in_range(c, lims):
            return coord, None
        air.add(c)
        for cube in surrounding_cubes(*c):
            if cube in cube_coords:
                seen.add(cube)
            elif cube not in air:
                qq.append(cube)
    return list(air), list(seen)

def min_axis(grid, axis):
    return min([x[axis] for x in grid])

def max_axis(grid, axis):
    return max([x[axis] for x in grid])

def get_limits(grid):
    xmin, xmax = min_axis(grid, 0), max_axis(grid, 0)
    ymin, ymax = min_axis(grid, 1), max_axis(grid, 1)
    zmin, zmax = min_axis(grid, 2), max_axis(grid, 2)
    return ((xmin, xmax), (ymin, ymax), (zmin, zmax))

class Area():
    def __init__(self, input):
        self.cubes = {x:Cube(x) for x in parse(input)}
        self.grid = set()
        for cube in self.cubes.values():
            self.grid.add(cube.coords)

    def check_cubes(self):
        for cube in self.cubes.values():
            for cube2 in self.cubes.values():
                if cube is not cube2 and cube2 not in cube.connected:
                    if is_adjacent(*cube.coords, *cube2.coords):
                        cube.connected.add(cube2.coords)
                        cube2.connected.add(cube.coords)

    def open_sides(self, exclude_internal=False):
        n = 0
        for cube in self.cubes.values():
            if exclude_internal:
                n += 6 - len(cube.connected) - len(cube.internal)
            else:
                n += 6 - len(cube.connected)
        return n

    def external_sides(self):
        lims = get_limits(self.grid)
        xrng = range(lims[0][0], lims[0][1] + 1)
        yrng = range(lims[1][0], lims[1][1], + 1)
        zrng = range(lims[2][0], lims[2][1], + 1)
        found_air = set()
        for x in xrng:
            for y in yrng:
                for z in zrng:
                    if (x, y, z) not in self.grid and (x, y, z) not in found_air:
                        air, adj_cubes = air_pocket((x, y, z), self.grid, lims)
                        if adj_cubes is not None:
                            if not isinstance(air, list):
                                air = [air]
                            for a in air:
                                found_air.add(a)
                            for cube in adj_cubes:
                                for a in air:
                                    if is_adjacent(*cube, *a):
                                        self.cubes[cube].internal.add(a)
        return self.open_sides(True)

input = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

input = open('data/day18.txt').read()    
a = Area(input)
a.check_cubes()
print(a.open_sides())

# part two
a = Area(input)
a.check_cubes()
print(a.external_sides())

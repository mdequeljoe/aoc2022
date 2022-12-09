x = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

x = open('data/day07.txt').read()

def path_str(path):
    return "/".join(path)

def parse(x):
    x = [x.split(" ") for x in x.splitlines()]
    dirs, path, current_path = {}, [], ''
    for line in x:
        path = path[:]
        if line[1] == "cd":
            dir = line[2]
            if dir == "..":
                path.pop()
            else:
                path.append(dir)
                current_path = path_str(path)
                if current_path not in dirs.keys():
                    dirs[current_path] = {'path':path, 'dirs':[], 'files':{}}
            continue
        elif line[1] == "ls":
            continue
        elif line[0] == "dir":
            dir_path = dirs[current_path]['path'][:]
            dir_path.append(line[1])
            dirs[current_path]['dirs'].append(path_str(dir_path))
        else:
            size, file = line
            dirs[current_path]['files'][file] = int(size)
    return dirs

def get_dir_size(dirs, dir):
    total = 0
    for file in dirs[dir]['files']:
        total += dirs[dir]['files'][file]
    for sub_dir in dirs[dir]['dirs']:
        total += get_dir_size(dirs, sub_dir)
    return total

x = parse(x)
sizes = [get_dir_size(x, k) for k in x]
ans = sum([s for s in sizes if s <= 100000])
print(ans)
      
# part two
def del_smallest_dir(dirs, space=70_000_000, unused_space=30_000_000):
    total_size = get_dir_size(dirs, "/")
    deletion_size = unused_space - (space - total_size)
    sizes = [get_dir_size(dirs, k) for k in dirs]
    return min([s for s in sizes if s >= deletion_size])

print(del_smallest_dir(x))
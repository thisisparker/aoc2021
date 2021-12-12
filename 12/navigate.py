from collections import defaultdict

with open('cavemap.txt') as f:
    lines = [l.strip() for l in f.readlines()]

caves = []

for l in lines:
    for c in l.split('-'):
        if c not in caves:
            caves.append(c)
small = [c for c in caves if c not in ['start', 'end'] and c[0].islower()]
big = [c for c in caves if c[0].isupper()]

print(small)
print(big)

connections = defaultdict(list)

for l in lines:
    cave1, cave2 = l.split('-')
    connections[cave1].append(cave2)
    connections[cave2].append(cave1)

print(connections)

paths = []

def no_small_multiples(path):
    return not(any(path.count(c) > 1 for c in small))

def extend_path(current_path, part2=False):
    for c in connections[current_path[-1]]:
        if c in big:
            extend_path(current_path[:] + [c], part2)
        elif not part2 and c in small and c not in current_path[:-1]:
            extend_path(current_path[:] + [c], part2)
        elif part2 and c in small:
            if c not in current_path[:-1]:
                extend_path(current_path[:] + [c], part2)
            elif no_small_multiples(current_path):
                extend_path(current_path[:] + [c], part2)
        elif c == 'end':
            paths.append(current_path + [c])

extend_path(['start'], part2=False)
print(len(paths))

paths = []
extend_path(['start'], part2=True)
print(len(paths))

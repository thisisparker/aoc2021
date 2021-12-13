with open('input.txt') as f:
    points = [l.strip().split(',') for l in f.readlines() 
                  if l.strip() and  not l.startswith('fold')]

points = [(int(c[0]), int(c[1])) for c in points]

with open('input.txt') as f:
    folds = [l.strip() for l in f.readlines() if l.startswith('fold')]

folds = [f[len('fold along '):] for f in folds]
folds = [f.split('=') for f in folds]
folds = [(f[0], int(f[1])) for f in folds]

def fold_sheet(point_list, f):
    new_sheet = []
    for p in point_list:
        if f[0] == 'x':
            new_point = p if f[1] > p[0] else (2*f[1] - p[0], p[1])
        elif f[0] == 'y':
            new_point = p if f[1] > p[1] else (p[0], (2*f[1] - p[1]))
        new_sheet.append(new_point)

    return new_sheet

print(len(points))
folded_points = points[:]
for f in folds:
    folded_points = fold_sheet(folded_points, f)
    folded_points = list(set(folded_points))
    print(len(folded_points))

max_x = max(folded_points, key=lambda x: x[0])[0]
max_y = max(folded_points, key=lambda x: x[1])[1]

lines= []
for y in range(max_y+1):
    line = ''
    for x in range(max_x+1):
        line += '#' if (x,y) in folded_points else ' '
    lines.append(line)

print(*lines, sep='\n')

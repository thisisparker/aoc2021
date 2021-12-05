from collections import Counter

with open('vents.txt') as f:
    lines = [l.strip() for l in f.readlines()]

lines = [l.split('->') for l in lines]

parsed_lines = []

for l in lines:
    parsed={}
    parsed['x1'], parsed['y1'] = [int(i) for i in l[0].split(',')]
    parsed['x2'], parsed['y2'] = [int(i) for i in l[1].split(',')]
    parsed_lines.append(parsed)

hv_points = []
all_points = []

for l in parsed_lines:
    if l['x1'] == l['x2']:
        start_y, end_y = sorted([l['y1'], l['y2']])
        hv_points.extend([(l['x1'],y) for y in range(start_y, end_y + 1)])
    elif l['y1'] == l['y2']:
        start_x, end_x = sorted([l['x1'], l['x2']])
        hv_points.extend([(x,l['y1']) for x in range(start_x, end_x + 1)])
    else:
        start_x, end_x = l['x1'], l['x2']
        x_dir = 1 if end_x > start_x else -1
        start_y, end_y = l['y1'], l['y2']
        y_dir = 1 if end_y > start_y else -1
        y = start_y
        for x in range(start_x, end_x + x_dir, x_dir): 
            all_points.append((x,y))
            y += y_dir

all_points.extend(hv_points)

c = Counter(hv_points)
repeats = len([i for i in c if c[i] >= 2])

print('part i: there are {} points that appear twice on horizontal/vertical lines'.format(repeats))

c = Counter(all_points)
repeats = len([i for i in c if c[i] >= 2])

print('part ii: {} repeats this time'.format(repeats))


with open('altitudes.txt') as f:
    rows = [d.strip() for d in f.readlines()]

for i, row in enumerate(rows):
    rows[i] = [int(d) for d in row]

low_points = []
low_coords = []

for x in range(len(rows[0])):
    for y in range(len(rows)):
        above = rows[x][y-1] if y > 0 else 10
        left = rows[x-1][y] if x > 0 else 10
        right = rows[x+1][y] if x < (len(rows[0]) - 1) else 10
        below = rows[x][y+1] if y < (len(rows) - 1) else 10

        if rows[x][y] < above and rows[x][y] < below and rows[x][y] < left and rows[x][y] < right:
            low_points.append(rows[x][y])
            low_coords.append((x,y))

print(sum(low_points) + len(low_points))

basins = []

def check_adjacents(coord, rows, basin=set()):
    x, y = coord
    height = rows[x][y]
    basin.add(coord)
    above = rows[x][y-1] if y > 0 else 10
    left = rows[x-1][y] if x > 0 else 10
    right = rows[x+1][y] if x < (len(rows[0]) - 1) else 10
    below = rows[x][y+1] if y < (len(rows) - 1) else 10

    if height < above < 9 and (x,y-1) not in basin:
        basin.update(check_adjacents((x, y-1), rows, basin))

    if height < left < 9 and (x-1,y) not in basin:
        basin.update(check_adjacents((x-1, y), rows, basin))

    if height < right < 9 and (x+1, y) not in basin:
        basin.update(check_adjacents((x+1, y), rows, basin))

    if height < below < 9 and (x, y+1) not in basin:
        basin.update(check_adjacents((x, y+1), rows, basin))
    
    return basin
    
for coord in low_coords:
    b = check_adjacents(coord, rows, basin=set())
    basins.append(b)

basins.sort(key=len, reverse=True)

print(len(basins[0]) * len(basins[1]) * len(basins[2]))


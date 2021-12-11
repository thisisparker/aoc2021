with open('input.txt') as f:
    octopi = [[int(c) for c in l.strip()] for l in f.readlines()]

global_flash_count = 0

def step(octopi):
    flashes = []
    octopi = [[val + 1 for val in row] for row in octopi]

    flashes = [(x, y) for y, row in enumerate(octopi) 
                      for x, val in enumerate(row) if octopi[y][x] > 9]

    i = 0
    while i < len(flashes):
        x, y = flashes[i]
        octopi, new_flashes = flash(x, y, octopi)
        flashes.extend([f for f in new_flashes if f not in flashes])
        i += 1 

    global global_flash_count

    superflash = True if len(flashes) == 100 else False

    for coord in flashes:
        x, y = coord
        octopi[y][x] = 0
        global_flash_count += 1


    return octopi, superflash
                

def flash(x, y, octopi):
    affected_coords = [(x-1, y-1), (x, y-1), (x+1, y-1),
                       (x-1, y),   (x, y),   (x+1, y),
                       (x-1, y+1), (x, y+1), (x+1, y+1)]

    affected_coords = [c for c in affected_coords if 0 <= c[0] < len(octopi[0]) 
                                                  and 0 <= c[1] < len(octopi)]

    new_flashes = []
    for c in affected_coords:
        octopi[c[1]][c[0]] += 1
        if octopi[c[1]][c[0]] > 9:
            new_flashes.append(c)

    return octopi, new_flashes
         

for _ in range(1000):
    octopi, superflash = step(octopi)
    if _ == 100:
        print(global_flash_count)
    if superflash:
        print(_ + 1)
        break

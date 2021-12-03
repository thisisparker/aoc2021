with open('directions.txt') as f:
    directions = [l.strip() for l in f.readlines()]

depth = 0
pos = 0

for d in directions:
    direction = d.split()[0]
    amount = int(d.split()[1])

    if direction == 'up':
        depth -= amount
    elif direction == 'down':
        depth += amount
    elif direction == 'forward':
        pos += amount

print(f'final depth is {depth}, final position is {pos}')
print(f'product is {depth * pos}')


depth = 0
pos = 0
aim = 0

for d in directions:
    direction = d.split()[0]
    amount = int(d.split()[1])

    if direction == 'up':
        aim -= amount
    elif direction == 'down':
        aim += amount
    elif direction == 'forward':
        pos += amount
        depth += aim * amount

print('part ii')

print(f'final depth is {depth}, final position is {pos}')
print(f'product is {depth * pos}')

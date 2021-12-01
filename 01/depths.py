with open('depths.txt') as f:
    depths = [int(d) for d in f.readlines()]

drops = [depths[i] for i in range(1, len(depths)) if depths[i] > depths[i-1]]

print(f'there are {len(drops)} drops')

groupings = [depths[i:i+3] for i in range(len(depths) - 2)]

group_drops = [groupings[i] for i in range(1, len(groupings)) if sum(groupings[i]) > sum(groupings[i-1])]

print(f'there are {len(group_drops)} drops of a rolling 3-measurement average')

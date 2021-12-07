with open('positions.txt') as f:
    positions = [int(i) for i in f.read().split(',')]

spots = {}

for i in range(min(positions), max(positions)):
    total_moves = 0
    for p in positions:
        total_moves += abs(i-p)
    spots[i] = total_moves

optimal_spot = min(spots.keys(), key=lambda x: spots[x])

print(optimal_spot, spots[optimal_spot])

spots = {}

for i in range(min(positions), max(positions)):
    total_fuel = 0
    for p in positions:
        total_fuel += sum(range(abs(i-p) + 1))
    spots[i] = total_fuel

optimal_spot = min(spots.keys(), key=lambda x: spots[x])

print(optimal_spot, spots[optimal_spot])

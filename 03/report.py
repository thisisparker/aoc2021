with open('diagnostic.txt') as f:
    diags = [l.strip() for l in f.readlines()]


def get_readings(values):
    gamma = ''
    epsilon = ''

    for d in range(len(values[0])):
        l = [entry[d] for entry in values]
        if l.count('0') > l.count('1'):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return gamma, epsilon

gamma, epsilon = get_readings(diags)

print(f'gamma and epsilon values are {gamma} and {epsilon}')
print(f'those translate to {int(gamma, 2)} and {int(epsilon, 2)}')
print(f'their product is {int(gamma,2) * int(epsilon,2)}')

oxygen_ratings = diags[:]
co2_ratings = diags[:]

for d in range(len(oxygen_ratings[0])):
    gamma, epsilon = get_readings(oxygen_ratings)
    oxygen_ratings = [v for v in oxygen_ratings if v[d] == gamma[d]]
    if len(oxygen_ratings) == 1:
        break

for d in range(len(co2_ratings[0])):
    print(len(co2_ratings))
    gamma, epsilon = get_readings(co2_ratings)
    co2_ratings = [v for v in co2_ratings if v[d] == epsilon[d]]
    if len(co2_ratings) == 1:
        break
        
print(f'oxygen rating is {oxygen_ratings}, co2 is {co2_ratings}')
print(f'multiplied: {int(oxygen_ratings[0], 2) * int(co2_ratings[0], 2)}')

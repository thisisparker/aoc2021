from collections import defaultdict

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

template = lines.pop(0)

insertions = {l.split(' -> ')[0]:l.split(' -> ')[1] for l in lines}

def step(polymer_string):
    new_string = ''
    for i in range(0, len(polymer_string) - 1):
        new_string += polymer_string[i]
        new_string += insertions[polymer_string[i:i+2]]

    new_string += polymer_string[-1]

    return new_string

def step2(counter_of_pairs):
    starting_count = counter_of_pairs.copy()
    for k in starting_count.keys():
        counter_of_pairs[k] -= starting_count[k]
        counter_of_pairs[k[0] + insertions[k]] += starting_count[k]
        counter_of_pairs[insertions[k] + k[1]] += starting_count[k]
    
    return counter_of_pairs

ps = template

for _ in range(10):
    ps = step(ps)

c = defaultdict(int)
for l in ps:
    c[l] += 1

most_common = max(c, key=lambda x: c[x])
least_common = min(c, key=lambda x: c[x])
print(c[most_common] - c[least_common])

q = defaultdict(int)
for i in range(0, len(template) - 1):
    q[template[i:i+2]] += 1

for _ in range(40):
    q = step2(q)

j = defaultdict(int)
for k in q:
    j[k[0]] += q[k]

j[template[-1]] += 1
most_common = max(j, key=lambda x: j[x])
least_common = min(j, key=lambda x: j[x])

print(most_common, j[most_common])
print(least_common, j[least_common])
print(j[most_common] - j[least_common])

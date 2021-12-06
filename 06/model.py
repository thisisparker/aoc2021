from collections import defaultdict

with open('fish_ages.txt') as f:
    fish_ages = [int(i) for i in f.read().split(',')]

def fish_day(fish_list):
    fish_list = [f - 1 for f in fish_list]
    for i, f in enumerate(fish_list):
        if f == -1:
            fish_list[i] = 6
            fish_list.append(8)
    return fish_list

for d in range(80):
    fish_ages = fish_day(fish_ages)

print('number of fish is {}'.format(len(fish_ages)))

with open('fish_ages.txt') as f:
    fish_ages = [int(i) for i in f.read().split(',')]

sea = defaultdict(int)

for fish in fish_ages:
    sea[fish] += 1

for i in range(256):
    newsea = defaultdict(int)

    for fish, count in sea.items():
        newfish = fish - 1
        if newfish < 0:
            newfish = 6
            newsea[8] += count
        newsea[newfish] += count

    sea = newsea

print(sum(sea.values()))

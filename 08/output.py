from collections import defaultdict

with open('segments.txt') as f:
    sequences = [l.strip() for l in f.readlines()]

patterns = []
outputs = []

for s in sequences:
    pattern, output = [w.strip() for w in s.split('|')]
    pattern = [set(p) for p in pattern.split(' ')]
    output = [set(o) for o in output.split(' ')]

    patterns.append(pattern)
    outputs.append(output)

uniques = 0

for o in outputs:
    for v in o:
        if len(v) == 2 or len(v) == 3 or len(v) == 4 or len(v) == 7:
            uniques += 1

print(uniques)

integer_outputs = []

for i in range(len(outputs)):
    int_out = []
    one, four, seven = None, None, None
    sequence = patterns[i] + outputs[i]

    for s in sequence:
        if len(s) == 2:
            one = s
        elif len(s) == 4:
            four = s
        elif len(s) == 3:
            seven = s
    
    for v in outputs[i]:
        if len(v) == 2:
            int_out.append(1)
        elif len(v) == 4:
            int_out.append(4)
        elif len(v) == 3:
            int_out.append(7)
        elif len(v) == 7:
            int_out.append(8)
        elif len(v) == 6:
            if four and v.issuperset(four):
                int_out.append(9)
            elif (one and v.issuperset(one)) or (seven and v.issuperset(seven)):
                int_out.append(0)
            elif one or four or seven:
                int_out.append(6)
        elif len(v) == 5:
            if (one and v.issuperset(one)) or (seven and v.issuperset(seven)):
                int_out.append(3)
            elif four and len(v.intersection(four)) == 2:
                int_out.append(2)
            elif four:
                int_out.append(5)
            else:
                print('yikes')

    integer_outputs.append(int_out)

final_integers = []

for o in integer_outputs:
    integer = int(''.join([str(i) for i in o]))
    final_integers.append(integer)

print(final_integers)

print(sum(final_integers))

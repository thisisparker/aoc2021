with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']

mismatches = []

for l in lines:
    opener_indexes = []
    mismatch = False
    for i, c in enumerate(l):
        if c in closers:
            match = openers[closers.index(c)]
            nonmatches = [o for o in openers if o != match]
            while i:
                if l[i] in nonmatches and i not in opener_indexes:
                    mismatch = c
                    break
                elif l[i] == match and i not in opener_indexes:
                    opener_indexes.append(i)
                    break
                i -= 1
            else:
                mismatch = c
        if mismatch:
            mismatches.append((l, mismatch))
            break

scoring = {')': 3,
           ']': 57,
           '}': 1197,
           '>': 25137}

score = 0
for m in mismatches:
    score += scoring[m[1]]

print(score)

noncorrupted = [l for l in lines if l not in [m[0] for m in mismatches]]
closing_strings = []

for l in noncorrupted:
    unclosed_chars = ''
    closer_indexes = []
    for i, c in enumerate(l[::-1]):
        if c in openers:
            match = closers[openers.index(c)]
            while i >= 0:
                if l[::-1][i] == match and i not in closer_indexes:
                    closer_indexes.append(i)
                    break
                i -= 1
            else:
                unclosed_chars += c
    closing_chars = ''
    for c in unclosed_chars:
        closing_chars += closers[openers.index(c)]
    closing_strings.append(closing_chars)

scoring = {')': 1,
           ']': 2,
           '}': 3,
           '>': 4}

string_scores = []

for s in closing_strings:
    score = 0
    for c in s:
        score = score * 5
        score += scoring[c]
    string_scores.append(score)

string_scores.sort()
print(string_scores[int(len(string_scores)/2)])

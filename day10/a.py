import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.read().strip().splitlines()

score_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

reverse = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

score_table2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

corrupted_lines = []

p1_score = 0
for line in data:
    opened = []
    for char in line:
        if char in '({[<':
            opened.append(char)
        else:
            if reverse[char] != opened[-1]:
                p1_score += score_table[char]
                corrupted_lines.append(line)
                break
            else:
                opened.pop()

for line in corrupted_lines:
    data.remove(line)

p2_scores = []
for line in data:
    opened = []
    for char in line:
        if char in '({[<':
            opened.append(char)
        else:
            opened.pop()
    temp_score = 0
    for x in reversed(opened):
        temp_score *= 5
        temp_score += score_table2[x]
        
    p2_scores.append(temp_score)

p2_scores.sort()

print(p1_score)
print(p2_scores[len(p2_scores)//2])

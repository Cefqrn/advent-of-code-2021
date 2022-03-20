import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.read().strip().split('\n')
    data = [x.split(' -> ') for x in data]
    data = [(x.split(','), y.split(',')) for x, y in data]
    data = [(list(map(int, x)), list(map(int, y))) for x, y in data]

p1 = 0
points = defaultdict(int)
for start, end in data:
    x1, y1 = start
    x2, y2 = end

    x1, x2 = min(x1, x2), max(x1,x2)
    y1, y2 = min(y1, y2), max(y1,y2)

    if x1 == x2:
        for y in range(y1, y2+1):
            points[(x1, y)] += 1
            if points[(x1, y)] == 2:
                p1 += 1
    elif y1 == y2:
        for x in range(x1, x2+1):
            points[(x, y1)] += 1
            if points[(x, y1)] == 2:
                p1 += 1

print(p1)

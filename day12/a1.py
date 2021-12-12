import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = [x.split('-') for x in f.read().splitlines()]

adjacent = defaultdict(list)
for start, end in data:
    adjacent[start].append(end)
    adjacent[end].append(start)

def explore(start, explored):
    path_count = 0
    for cave in adjacent[start]:
        if cave not in explored:
            if cave.islower():
                if cave == "end":
                    path_count += 1
                    continue
                path_count += explore(cave, explored | {cave})
            else:
                path_count += explore(cave, explored)
    return path_count

print(explore("start", {"start"}))
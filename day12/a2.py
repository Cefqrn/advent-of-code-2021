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
    if any(map(lambda x: x > 1, explored.values())):
        for cave in adjacent[start]:
            if cave == "end":
                path_count += 1
                continue
            if explored[cave] < 1:
                if cave.islower():
                    e = explored.copy()
                    e[cave] += 1
                    path_count += explore(cave, e)
                else:
                    path_count += explore(cave, explored)
    else: 
        for cave in adjacent[start]:
            if cave == "start":
                continue
            if cave == "end":
                path_count += 1
                continue
            
            if explored[cave] < 2:
                if cave.islower():
                    e = explored.copy()
                    e[cave] += 1
                    path_count += explore(cave, e)
                else:
                    path_count += explore(cave, explored)
    return path_count

explored = defaultdict(int)
explored["start"] += 1
print(explore("start", explored))
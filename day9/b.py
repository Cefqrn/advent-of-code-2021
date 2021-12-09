import os

ADJACENT = ((1, 0), (0, 1), (-1, 0), (0, -1))

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = [list(map(int, x)) for x in f.read().strip().split('\n')]

flagged = set()

def flag_basin(x, y):
    if (x, y) in flagged:
        return 0

    flagged.add((x, y))

    size = 1
    for dx, dy in ADJACENT:
        if x + dx < 0 or y + dy < 0 or y + dy >= len(data) or x + dx >= len(data[0]):
            continue
            
        if data[y+dy][x+dx] == 9:
            continue
        
        size += flag_basin(x+dx, y+dy)
    return size

basin_sizes = []
p1 = 0
for y, line in enumerate(data):
    for x, point in enumerate(line):
        if point < 9 and (x, y) not in flagged:
            basin_sizes.append(flag_basin(x, y))

        for dx, dy in ADJACENT:
            if x + dx < 0 or y + dy < 0:
                continue
            try:
                if point >= data[y+dy][x+dx]:
                    break
            except IndexError:
                pass
        else: # if the point is lower than all its neighbours
            p1 += point + 1

basin_sizes.sort()
p2 = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

print(p1)
print(p2)

import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    d = f.read().split('\n\n')
    points = {tuple(map(int, z.split(','))) for z in d[0].splitlines()}
    instructions = [z.split("=") for z in d[1].splitlines()]
    instructions = [[x[-1], int(y)] for x, y in instructions]

for direction, fold in instructions:
    new_points = set()
    if direction == "x":
        while points:
            x, y = points.pop()
            new_points.add((fold-abs(x-fold), y))
    else:
        while points:
            x, y = points.pop()
            new_points.add((x, fold-abs(y-fold)))
    points = new_points.copy()

xmin = min(points, key=lambda x: x[0])[0]
ymin = min(points, key=lambda x: x[1])[1]
xmax = max(points, key=lambda x: x[0])[0]
ymax = max(points, key=lambda x: x[1])[1]

grid = [[' ' for _ in range(xmin, xmax+1)] for _ in range(ymin, ymax+1)]

for x, y in points:
    grid[y][x] = '█'

for y in grid:
    for x in y:
        print(f'{x}', end='')
    print()
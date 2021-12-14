import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    d = f.read().split('\n\n')
    points = {tuple(map(int, z.split(','))) for z in d[0].splitlines()}
    instructions = [z.split("=") for z in d[1].splitlines()]
    instructions = [[x[-1], int(y)] for x, y in instructions]

direction, fold = instructions[0]
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

print(len(new_points))
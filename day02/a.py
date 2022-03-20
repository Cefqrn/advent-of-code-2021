import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.read().strip().split('\n')

x = 0
y1 = 0
y2 = 0
aim = 0
for command in data:
    dir, m = command.split()
    m = int(m)
    if dir == "forward":
        x += m
        y2 += aim * m
    if dir == "down":
        y1 += m
        aim += m
    if dir == "up":
        y1 -= m
        aim -= m

print(x*y1, x*y2)

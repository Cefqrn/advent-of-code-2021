import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    x, y = f.read()[13:].strip().split(', ')
    xmin, xmax = map(int, x[2:].split('..'))
    ymin, ymax = map(int, y[2:].split('..'))

x = y = 0

bestyv = 0
for syv in range(500):
    x = y = 0
    xv = 19
    yv = syv
    while x <= xmax and y >= ymin:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            bestyv = syv
            break

        x += xv
        y += yv
        xv = max(xv - 1, 0)
        yv -= 1     

ys = []
x = y = 0
xv = 19
yv = bestyv
print(bestyv)
while x <= xmax and y >= ymin:
    ys.append(y)
    x += xv
    y += yv
    xv = max(xv - 1, 0)
    yv -= 1

print(max(ys))
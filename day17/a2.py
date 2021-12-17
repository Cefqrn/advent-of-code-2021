import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    x, y = f.read()[13:].strip().split(', ')
    xmin, xmax = map(int, x[2:].split('..'))
    ymin, ymax = map(int, y[2:].split('..'))

xs = []
for syx in range(19, 202):
    s = 0
    x = 0
    xv = syx
    while x < xmax and not (x < xmin and xv == 0):
        x += xv
        xv = max(xv - 1, 0)
        s += 1
        if xmin <= x <= xmax:
            cte = 2 # ????? why does this work
            while x + xv < xmax:
                x += xv
                xv = max(xv - 1, 0)
                if x + xv < xmax:
                    cte += 1
                    if cte > 250:
                        break
            xs.append([syx, s, cte])
            break

p2 = 0
for syx in xs:
    for syv in range(-110, 111):
        x = y = 0
        xv, s, cte = syx
        yv = syv

        for _ in range(s+cte):
            x += xv
            y += yv
            xv = max(xv - 1, 0)
            yv -= 1
            if xmin <= x <= xmax and ymin <= y <= ymax:
                p2 += 1
                break

print(p2)
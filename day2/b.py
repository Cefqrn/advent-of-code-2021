import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = [(x[0], int(y)) for x, y in map(str.split, f.readlines())]

x = y = z = a = 0

for d, m in data:
    if d == "f":
        x += m
        z += a * m
    m *= dict(d=1,u=-1).get(d,0)
    a += m
    y += m

print(x*y, x*z)
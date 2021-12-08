import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    *data, = map(lambda x: [y.split() for y in  str.split(x, '|')], f.read().strip().split('\n'))

p1 = 0
p2 = 0
for inp, out in data:
    output = 0
    
    inputs = ''

    inp = tuple(map(lambda x: set(x), sorted(inp, key=len)))
    m = {}

    m[1] = inp[0]
    m[7] = inp[1]
    m[4] = inp[2]
    m[8] = inp[9]
    for n in inp[3:6]:
        if m[7] <= n:
            m[3] = n
        elif len(n & m[4]) == 2:
            m[2] = n
        else:
            m[5] = n
    for n in inp[6:9]:
        if m[5] <= n and m[1] <= n:
            m[9] = n
        elif m[5] <= n:
            m[6] = n
        else:
            m[0] = n

    for i, num in enumerate(out):
        for j, x in m.items():
            if set(num) == x:
                break
        output += 10**(3-i) * j
    p2 += output

print(p1, p2)
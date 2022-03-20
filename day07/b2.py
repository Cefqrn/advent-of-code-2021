import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    *data, = map(int, f.read().strip().split(','))

min_pos = min(data)
max_pos = max(data)

fuel_reqs = defaultdict(int)
fuel_req = 0
for x in range(min_pos, max_pos):
    for y in data:
        n = abs(y-x)
        fuel_reqs[x] += n*(n+1)//2

print(fuel_reqs[min(fuel_reqs, key=lambda x: fuel_reqs[x])])
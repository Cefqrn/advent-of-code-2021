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
        fuel_reqs[x] += sum(range(1,abs(y-x)+1))

print(fuel_reqs[min(fuel_reqs, key=lambda x: fuel_reqs[x])])
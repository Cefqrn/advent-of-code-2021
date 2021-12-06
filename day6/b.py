import os
from collections import deque

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    *data, = map(int, f.read().strip().split(','))

fish = deque([0]*9, maxlen=9)
for x in data:
    fish[x] += 1

for i in range(80):
    fish.rotate(-1)
    fish[6] += fish[8]

# part 1
print(sum(fish))

for i in range(256-80):
    fish.rotate(-1)
    fish[6] += fish[8]

# part 2
print(sum(fish))

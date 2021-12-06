import os
from collections import deque

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    *data, = map(int, f.read().strip().split(','))

fish = deque([0,0,0,0,0,0,0], maxlen=7)
for x in data:
    fish[x] += 1

eight = 0
seven = 0
for i in range(80):
    t = fish[0]
    fish.rotate(-1)
    fish[6] += seven
    seven = eight
    eight = t
    sevent, eight = eight, t

# part 1
print(sum(fish)+seven+eight)

for i in range(256-80):
    t = fish[0]
    fish.rotate(-1)
    fish[6] += seven
    seven = eight
    eight = t

# part 2
print(sum(fish)+seven+eight)

import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = list(map(int, f.read().split()))

part1 = 0
for l, l1 in zip(data, data[1:]):
    if l1 > l:
        part1 += 1

print(part1)

part2 = 0
for l1, l4 in zip(data, data[3:]):
    if l4 > l1:
        part2 += 1

print(part2)
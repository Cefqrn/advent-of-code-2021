import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = list(map(int, f.read().split()))

print(sum(l2>l1 for l1, l2 in zip(data, data[1:])))
print(sum(l4>l1 for l1, l4 in zip(data, data[3:])))
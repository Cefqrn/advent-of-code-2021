import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.readlines()

onecounts = [0] * 12
nilcounts = [0] * 12
for line in data:
    for i, char in enumerate(line):
        if char == "1":
            onecounts[i] += 1
        if char == "0":
            nilcounts[i] += 1

gamma = 0
epsilon = 0
for x in range(12):
    gamma <<= 1
    epsilon <<= 1
    if onecounts[x] > nilcounts[x]:
        gamma += 1
    else:
        epsilon += 1

print(gamma * epsilon)
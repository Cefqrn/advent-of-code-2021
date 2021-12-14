import os
from collections import defaultdict
from copy import deepcopy

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.read().split('\n\n')
    template, rules = data
    rules = [x.split(' -> ') for x in rules.splitlines()]
    rules = dict(rules)

pair_counts = defaultdict(int)
for i, pair in enumerate(zip(template, template[1:])):
    pair_counts[''.join(pair)] += 1

rules2 = {}
for pair, inserted_char in rules.items():
    rules2[pair] = (pair[0] + inserted_char, inserted_char + pair[1])

for x in range(10):
    for pair, count in tuple(pair_counts.items()):
        if pair in rules2 and count:
            for pair2 in rules2[pair]:
                pair_counts[pair2] += count
            pair_counts[pair] -= count
    
c = defaultdict(int)
for pair, count in pair_counts.items():
    c[pair[1]] += count

print(c[max(c, key=lambda x: c[x])] - c[min(c, key=lambda x: c[x])])

for x in range(30):
    for pair, count in tuple(pair_counts.items()):
        if pair in rules2 and count:
            for pair2 in rules2[pair]:
                pair_counts[pair2] += count
            pair_counts[pair] -= count

c = defaultdict(int)
for pair, count in pair_counts.items():
    c[pair[1]] += count

print(c[max(c, key=lambda x: c[x])] - c[min(c, key=lambda x: c[x])])
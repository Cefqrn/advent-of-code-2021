import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.read().strip().split()

nums = data.copy()

i = 0
remainder = nums.copy()
while len(remainder) > 1:
    onecount = 0
    nilcount = 0
    for line in remainder:
        if line[i] == "1":
            onecount += 1
        else:
            nilcount += 1
    for num in remainder.copy():
        if num[i] == ("1" if onecount >= nilcount else "0"):
            continue
        remainder.remove(num)
    i += 1
o2 = int(remainder[0], 2)


i = 0
remainder = nums.copy()
while len(remainder) > 1:
    onecount = 0
    nilcount = 0
    for line in remainder:
        if line[i] == "1":
            onecount += 1
        else:
            nilcount += 1
    for num in remainder.copy():
        if num[i] == ("0" if onecount >= nilcount else "1"):
            continue
        remainder.remove(num)
    i += 1

co2 = int(remainder[0], 2)

print(o2*co2)

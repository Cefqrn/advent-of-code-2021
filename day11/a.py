import os

NEIGHBORS = [(x, y) for x in range(-1, 2) for y in range(-1,2) if x != 0 or y != 0]

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.read().strip().splitlines()
    data = [list(map(int, x)) for x in data]

flashing = []
flashed = []

tot_flashes = 0
num_flashes = 0

step_num = 0

while num_flashes != 100:
    num_flashes = 0
    step_num += 1
        
    for y, line in enumerate(data):
        for x, value in enumerate(line):
            data[y][x] += 1

    flag = True
    while flag:
        flag = False
        for y, line in enumerate(data):
            for x, value in enumerate(line):
                if data[y][x] > 9:
                    if (x, y) not in flashed:
                        num_flashes += 1
                        flag = True
                        flashing.append((x,y))
        while flashing:
            x, y = flashing.pop()
            for dx, dy in NEIGHBORS:
                if x + dx < 0 or y + dy < 0: continue
                try:
                    data[y+dy][x+dx] += 1
                except IndexError:
                    pass
            flashed.append((x, y))
    
    while flashed:
        x, y = flashed.pop()
        data[y][x] = 0
    
    if step_num <= 100:
        tot_flashes += num_flashes

print(tot_flashes)
print(step_num)
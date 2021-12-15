import os
from collections import defaultdict

NEIGHBORS = [0,1],[1,0],[-1,0],[0,-1]

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = [list(map(int, x)) for x in f.read().splitlines()]

def returnInf():
    return 999999999999

def h(x, y):
    return x - len(data) + y - len(data)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return list(reversed(total_path))

def explore(start, goal, h):
    open_set = {start}
    came_from = {}

    g_score = defaultdict(returnInf)
    f_score = defaultdict(returnInf)

    g_score[start] = 0
    f_score[start] = h(*start)

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        x, y = current

        if current == goal:
            return reconstruct_path(came_from, current)
        
        open_set.remove(current)

        for dx, dy in NEIGHBORS:
            if x + dx < 0 or y + dy < 0 or x + dx >= len(data[0]) or y + dy >= len(data):
                continue

            neighbor = x + dx, y + dy

            tentative_gscore = g_score[current] + data[neighbor[1]][neighbor[0]]
            if tentative_gscore < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_gscore
                f_score[neighbor] = tentative_gscore + h(*neighbor)

                open_set.add(neighbor)

shortest_path = explore((0, 0), (len(data[0])-1, len(data)-1), h)
print(sum(map(lambda x: data[x[1]][x[0]], shortest_path)) - data[0][0])
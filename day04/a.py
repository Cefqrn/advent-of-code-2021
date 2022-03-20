import os

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = f.read().strip().split('\n')

pool = list(map(int, data[0].split(',')))
boards = [[[int(z) for z in y.split()] for y in data[x:x+5]] for x in range(2,len(data),6)]
drawn = set()

is_drawn = lambda x: x in drawn
is_not_drawn = lambda x: x not in drawn

def p1():
    for n in pool:
        drawn.add(n)
        for board in boards:
            for l in board:
                for c in l:
                    if c not in drawn:
                        break
                else:
                    print(sum(sum(filter(is_not_drawn, l)) for l in board) * n)
                    return
            for l in zip(*board):
                for c in l:
                    if c not in drawn:
                        break
                else:
                    print(sum(sum(filter(is_not_drawn, l)) for l in board) * n)
                    return

wins = []
def p2():
    for n in pool:
        drawn.add(n)
        for board in boards.copy():
            for l in board:
                for c in l:
                    if c not in drawn:
                        break
                else:
                    try:
                        wins.append(sum(sum(filter(is_not_drawn, l)) for l in board) * n)
                        boards.remove(board)
                    except:
                        pass
            for l in zip(*board):
                for c in l:
                    if c not in drawn:
                        break
                else:
                    try:
                        wins.append(sum(sum(filter(is_not_drawn, l)) for l in board) * n)
                        boards.remove(board)
                    except:
                        pass
                    
    print(wins[-1])
            

p1()
p2()

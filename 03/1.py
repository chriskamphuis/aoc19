import math
wire1 = []
wire2 = []
path = set()
with open('input.txt', 'r') as f:
    wire1 = f.readline().strip().split(',')
    wire2 = f.readline().strip().split(',')
current = [0, 0]
for entry in wire1:
    steps = int(entry[1:])
    direction = entry[0]
    while steps > 0:
        if direction == 'R':
            current[0] += 1
        elif direction == 'D':
            current[1] -= 1
        elif direction == 'L':
            current[0] -= 1
        else:
            current[1] += 1
        tmp = str(current[0]) + ',' + str(current[1])
        path |= {tmp}
        steps -= 1

current = [0, 0]
shortest = math.inf
for entry in wire2:
    steps = int(entry[1:])
    direction = entry[0]
    while steps > 0:
        if direction == 'R':
            current[0] += 1
        elif direction == 'D':
            current[1] -= 1
        elif direction == 'L':
            current[0] -= 1
        else:
            current[1] += 1
        tmp = str(current[0]) + ',' + str(current[1]) 
        if tmp in path:
            dist = sum([abs(a) for a in current])
            if dist < shortest:
                shortest = dist
        steps -= 1
print(shortest)

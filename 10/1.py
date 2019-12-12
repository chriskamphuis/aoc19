from collections import defaultdict

asteroids = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '#':
                asteroids.append((j, i))

def gcdiv(a, b):
    if a == 0:
        return (0, 1)
    if b == 0:
        return (1, 0)
    x, y = a, b
    while y:
        x, y = y, x%y
    return (a/x, b/x)


detectable = defaultdict(set)
maximum = 0
for i in range(len(asteroids)):
    for j in range(i+1, len(asteroids)):
        asteroid1 = asteroids[i]
        asteroid2 = asteroids[j]
        dx, dy = asteroid2[0] - asteroid1[0], asteroid2[1] - asteroid1[1]
        dir_x, dir_y = gcdiv(dx, dy)
        detectable[i] |= {(dir_x, dir_y)}
        detectable[j] |= {(-dir_x, -dir_y)}
    if len(detectable[i]) > maximum:
        maximum = len(detectable[i]) 

print(maximum)

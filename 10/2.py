from collections import defaultdict
import math

asteroids = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '#':
                asteroids.append((j, i))

def gcdiv(a, b):
    if a == 0:
        return (0, b/(abs(b)))
    if b == 0:
        return (a/(abs(a)), 0)
    x, y = abs(a), abs(b)
    while y:
        x, y = y, x%y
    return (a/x, b/x)

detectable = defaultdict(set)
maximum = 0
best = None
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
        best = i

ims = asteroids[best]
# Get asteroids on all angles that are the closest
# 200 < number of maximum so we do not care about asteroids that are behind others

eucledian = lambda a, b : math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
angles = set()
seeables = defaultdict(int)
nearest = dict()

for i in range(len(asteroids)):
    if ims == asteroids[i]:
        continue 
    asteroid = asteroids[i]
    dx, dy = asteroid[0] - ims[0], asteroid[1] - ims[1]
    dir_x, dir_y = gcdiv(dx, dy)
    direction = (dir_x, dir_y)
    angles |= {direction}
    dist = eucledian(ims, asteroid) 
    if seeables[direction] == 0 or seeables[direction] > dist:
        seeables[direction] = dist

start_direction = (0, 1)

keys = list(seeables.keys())
norms = [math.sqrt(k[0]**2 + k[1]**2) for k in keys]
normalized_keys = [(k[0]/norm, k[1]/norm) for k, norm in zip(keys, norms)]
order = sorted([(int(norm_key[0]<0), eucledian(norm_key, start_direction), key) for norm_key, key in zip(normalized_keys, keys)])
twohunderd = order[200-1][2]
scale = seeables[twohunderd] / math.sqrt(twohunderd[0]**2 + twohunderd[1]**2)
print(round((ims[0]+twohunderd[0]*scale) * 100 + (ims[1]+twohunderd[1]*scale)))

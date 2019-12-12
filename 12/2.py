import re
import numpy as np
from math import gcd
from functools import reduce

coordinates = []
velocities = []
start_c = []
start_v = []

def lcm(a,b):
    return (a*b)//gcd(a,b)

def lcm_multiple(xs):
    return reduce(lcm, xs)

with open('input.txt', 'r') as f:
    for line in f:
        coor = [int(e) for e in re.findall(r'-?[0-9]+', line)]
        coordinates.append(coor)
        start_c.append(coor)
        
        vel = [0 for _ in coordinates[-1]]
        velocities.append(vel)
        start_v.append(vel)


rotation_time = [0, 0, 0]

count = 0
while not all(rotation_time):
    velocity_changes = []
    for i, coordinate1 in enumerate(coordinates):
        change = [0, 0, 0]
        for j, coordinate2 in enumerate(coordinates):
            if i == j:
                continue
            for c in range(len(coordinate1)):
                if coordinate1[c] < coordinate2[c]:
                    change[c] += 1
                elif coordinate1[c] > coordinate2[c]:
                    change[c] -= 1
                else:
                    continue
        velocity_changes.append(change) 
    velocities = [[old+update for old, update in zip(old, update)] for old, update in zip(velocities, velocity_changes)]
    coordinates = [[old+update for old, update in zip(old, update)] for old, update in zip(coordinates, velocities)]
    count += 1
    for i in range(3):
        if rotation_time[i] == 0 and [co[i] for co in coordinates] == [co[i] for co in start_c] and [v[i] for v in velocities] == [v[i] for v in start_v]:
            rotation_time[i] = count

def common_divisors(values):
    final = set()
    divisors = []
    smallest = min(values) 
    for i in range(2, round(smallest**0.5)):
        while smallest % i == 0:
            divisors.append(i) 
            smallest /= i
    for d in divisors:
        if all([v%d==0 for v in values]):
            final |= {d}
    return final


for c in common_divisors(rotation_time):
    while all([r%c==0 for r in rotation_time]):
        rotation_time = [int(r/c) for r in rotation_time]

print(np.prod(rotation_time))

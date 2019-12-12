import re
coordinates = []
velocities = []
with open('input.txt', 'r') as f:
    for line in f:
        coordinates.append([int(e) for e in re.findall(r'-?[0-9]+', line)])
        velocities.append([0 for _ in coordinates[-1]])

for step in range(1000):
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

pot = [sum([abs(v) for v in p]) for p in coordinates]
kin = [sum([abs(v) for v in k]) for k in velocities]
energy = sum([p * k for p, k in zip(pot, kin)])
print(energy)

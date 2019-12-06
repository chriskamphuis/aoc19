from collections import defaultdict
orbit_map = defaultdict(list)
froms = set()
toos = set()
with open('input.txt', 'r') as f:
    for line in f:
        source, orbiter = line.strip().split(')')
        orbit_map[source].append(orbiter)
        froms |= {source}
        toos |= {orbiter}
starts = {item for item in froms if item not in toos}

keys = list(starts)
iteration = 0
total_paths = 0
while len(keys) > 0:
    new_keys = []
    for k in keys:
        total_paths += iteration
        for v in orbit_map[k]:
            new_keys.append(v)
    keys = new_keys
    iteration += 1
print(total_paths)

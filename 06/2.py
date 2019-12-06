from collections import defaultdict
graph = defaultdict(list)
with open('input.txt', 'r') as f:
    for l in f:
        k, v = l.strip().split(')')
        graph[k].append(v)
        graph[v].append(k)

frontier = graph['YOU']
visited = {'YOU'}
length = 0
while True:
    new_frontier = set()
    for f in frontier:
        for k in graph[f]:
            if k not in visited:
                new_frontier |= {k}
        visited |= {f}
    if 'SAN' in new_frontier:
        break
    length += 1
    frontier = list(new_frontier)
print(length)

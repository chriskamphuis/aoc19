import math, random

reactions = dict()

with open('input.txt', 'r') as f:
    for line in f:
        before, after = [e.strip() for e in line.strip().split('=>')]
        elements = dict()
        for source in [e.strip() for e in before.split(',')]:
            amount, element = source.split(' ')
            elements[element] = int(amount)
        amount, element = after.split(' ')
        reactions[element] = (int(amount), elements)

need = [('FUEL', 1)]
spare = [('FUEL', 0)]
while len(need) != 1 or need[0][0] != 'ORE':
    n = random.choice(need) 
    if n[0] == 'ORE':
        continue
    need.remove(n)
    element = n[0]
    amount = n[1]
    sources = reactions[element]
    number = math.ceil(amount / sources[0])
    print(amount) 
    print(sources)
    print(number)
    for key, value in sources[1].items():
        for i, ne in enumerate(need):
            if ne[0] == key:
                need[i] = (ne[0], ne[1] + amount)
                spare[i] = (ne[0], amount - value * number)
                break
        else:
            need.append((key, value * number))
            spare.append((key, 0))
print(need)

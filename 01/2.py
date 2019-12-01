import math

def fuel(x):
    if x > 0:
        f = math.floor(x/3) - 2
        return f + fuel(f)
    else:
        return 0

with open('input.txt', 'r') as f:
    print(sum([fuel(int(l)) for l in f]))

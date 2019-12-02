lines = []
with open('input.txt', 'r') as f:
    lines = f.read().strip().split(',')
lines = [int(e) for e in lines]

def action(a, b):
    i = 0
    l = [a for a in lines]
    l[1] = a
    l[2] = b
    while True:
        action = l[i]
        if action == 99:
            break
        if action == 1:
            l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
        if action == 2:
            l[l[i+3]] = l[l[i+1]] * l[l[i+2]]
        i+=4
    return l[0]

def compute():
    for a in range(0, 100):
        for b in range(0, 100):
            res = action(a, b)
            if res == 19690720:
                return 100 * a + b
print(compute())

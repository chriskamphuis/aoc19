lines = []
with open('input.txt', 'r') as f:
    lines = f.read().strip().split(',')
lines = [int(e) for e in lines]
i = 0
lines[1] = 12
lines[2] = 2
while True:
    action = lines[i]
    if action == 99:
        break
    if action == 1:
        lines[lines[i+3]] = lines[lines[i+1]] + lines[lines[i+2]]
    if action == 2:
        lines[lines[i+3]] = lines[lines[i+1]] * lines[lines[i+2]]
    i+=4
print(lines[0])

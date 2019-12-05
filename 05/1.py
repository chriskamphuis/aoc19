instructions = []
with open('input.txt', 'r') as f:
   instructions = [int(a) for a in f.read().strip().split(',')]

input_value = 1
location = 0

while True:
    instruct = instructions[location]
    opcode = instruct % 100
    parameters = instruct // 100
    
    if opcode in [1, 2]:
        # addition or multiplication
        v1, v2 = 0, 0
        if parameters % 10 == 1: 
            v1 = instructions[location+1]
        else:
            v1 = instructions[instructions[location+1]]
        parameters //= 10
        if parameters % 10 == 1: 
            v2 = instructions[location+2]
        else:
            v2 = instructions[instructions[location+2]]
        v3 = instructions[location+3]
        if opcode == 1:
            instructions[v3] = v1 + v2
        else:
            instructions[v3] = v1 * v2
        location += 4
    elif opcode == 3:
        instructions[instructions[location+1]] = input_value
        location += 2
    elif opcode == 4:
        if parameters % 10 == 1:
            print(instructions[location+1], end='')
        else:
            print(instructions[instructions[location+1]], end='')
        location+=2
    elif opcode == 99:
        break

instructions = []
with open('input.txt', 'r') as f:
   instructions = [int(a) for a in f.read().strip().split(',')]

input_value = 5
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
        # Write input
        instructions[instructions[location+1]] = input_value
        location += 2
    elif opcode == 4:
        # Print output
        if parameters % 10 == 1:
            print(instructions[location+1], end='')
        else:
            print(instructions[instructions[location+1]], end='')
        location+=2
    elif opcode in [5, 6]:
        # jumps
        v1, v2 = 0, 0
        if parameters % 10 == 1: 
            v1 = instructions[location+1]
        else:
            v1 = instructions[instructions[location+1]]
        if v1 == 0 and opcode == 5 or v1 != 0 and opcode == 6:
            location += 3
            continue
        parameters //= 10
        if parameters % 10 == 1: 
            v2 = instructions[location+2]
        else:
            v2 = instructions[instructions[location+2]]
        location = v2
    elif opcode in [7, 8]:
        # Less than or equals
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
        if v1 < v2 and opcode == 7 or v1 == v2 and opcode == 8:
            instructions[v3] = 1
        else:
            instructions[v3] = 0
        location += 4
    elif opcode == 99:
        break

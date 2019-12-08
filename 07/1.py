from itertools import permutations

instructs = []
with open('input.txt', 'r') as f:
   instructs = [int(a) for a in f.read().strip().split(',')]

def thruster(instructions, inpt):
    location = 0
    output = ''
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
            instructions[instructions[location+1]] = inpt.pop()
            location += 2
        elif opcode == 4:
            # Print output
            if parameters % 10 == 1:
                output += str(instructions[location+1])
            else:
                output += str(instructions[instructions[location+1]])
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
            return int(output)

phases = [0, 1, 2, 3, 4]
initial_input = 0
max_score = 0
for phase in permutations(phases):
    i = initial_input
    for p in phase:
        outp = thruster(instructs, [i, p])
        i = outp
    if i > max_score:
        max_score = i
print(max_score)


from itertools import permutations
from queue import Queue

instructs = []
with open('input.txt', 'r') as f:
   instructs = [int(a) for a in f.read().strip().split(',')]

class thruster:

    def __init__(self, instructions, inpt):
        self.loc = 0
        self.instructions = instructions
        self.inputqueue = Queue()
        for i in inpt:
            self.inputqueue.put(i)

    def add_input(self, inpt):
        self.inputqueue.put(inpt)

    def thrust(self):
        while True:
            instruct = self.instructions[self.loc]
            opcode = instruct % 100
            parameters = instruct // 100
            if opcode in [1, 2]:
                # addition or multiplication
                v1, v2 = 0, 0
                if parameters % 10 == 1: 
                    v1 = self.instructions[self.loc+1]
                else:
                    v1 = self.instructions[self.instructions[self.loc+1]]
                parameters //= 10
                if parameters % 10 == 1: 
                    v2 = self.instructions[self.loc+2]
                else:
                    v2 = self.instructions[self.instructions[self.loc+2]]
                v3 = self.instructions[self.loc+3]
                if opcode == 1:
                    self.instructions[v3] = v1 + v2
                else:
                    self.instructions[v3] = v1 * v2
                self.loc+= 4
            elif opcode == 3:
                # Write input
                self.instructions[self.instructions[self.loc+1]] = self.inputqueue.get()
                self.loc += 2
            elif opcode == 4:
                # Print output
                output = ''
                if parameters % 10 == 1:
                    output += str(self.instructions[self.loc+1])
                else:
                    output += str(self.instructions[self.instructions[self.loc+1]])
                self.loc+=2
                return int(output)
            elif opcode in [5, 6]:
                # jumps
                v1, v2 = 0, 0
                if parameters % 10 == 1: 
                    v1 = self.instructions[self.loc+1]
                else:
                    v1 = self.instructions[self.instructions[self.loc+1]]
                if v1 == 0 and opcode == 5 or v1 != 0 and opcode == 6:
                    self.loc += 3
                    continue
                parameters //= 10
                if parameters % 10 == 1: 
                    v2 = self.instructions[self.loc+2]
                else:
                    v2 = self.instructions[self.instructions[self.loc+2]]
                self.loc = v2
            elif opcode in [7, 8]:
                # Less than or equals
                v1, v2 = 0, 0
                if parameters % 10 == 1: 
                    v1 = self.instructions[self.loc+1]
                else:
                    v1 = self.instructions[self.instructions[self.loc+1]]
                parameters //= 10
                if parameters % 10 == 1: 
                    v2 = self.instructions[self.loc+2]
                else:
                    v2 = self.instructions[self.instructions[self.loc+2]]
                v3 = self.instructions[self.loc+3]
                if v1 < v2 and opcode == 7 or v1 == v2 and opcode == 8:
                    self.instructions[v3] = 1
                else:
                    self.instructions[v3] = 0
                self.loc += 4
            elif opcode == 99:
                return None

inputs = [[9], [8], [7], [6], [5]]
max_score = 0

for inp in permutations(inputs):
    thrusters = [thruster(instructs.copy(), i) for i in inp]
    thrusters[0].add_input(0)
    output = 0
    while output is not None:
        for i in range(len(thrusters)):
            output = thrusters[i].thrust()
            thrusters[(i+1)%5].add_input(output)
        if output is not None and output > max_score:
            max_score = output
print(max_score)

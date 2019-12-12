from queue import Queue
from collections import defaultdict

instructions = []
with open('input.txt', 'r') as f:
   instructions = [int(a) for a in f.read().strip().split(',')]

class thruster:
    def __init__(self, instructions):
        self.input = Queue()
        self.location = 0
        self.relative_base = 0
        self.instructions = instructions
   
    def add_input(self, inp):
        self.input.put(inp)

    def thrust(self):
        while True:
            try: 
                instruct = self.instructions[self.location]
                opcode = instruct % 100
                parameters = instruct // 100
                if opcode in [1, 2]:
                    # addition or multiplication
                    v1, v2 = 0, 0
                    if parameters % 10 == 1: 
                        v1 = self.instructions[self.location+1]
                    elif parameters % 10 == 2:
                        v1 = self.instructions[relative_base + self.instructions[self.location+1]]
                    else:
                        v1 = self.instructions[self.instructions[self.location+1]]
                    parameters //= 10
                    if parameters % 10 == 1: 
                        v2 = self.instructions[self.location+2]
                    elif parameters % 10 == 2:
                        v2 = self.instructions[relative_base + self.instructions[self.location+2]]
                    else:
                        v2 = self.instructions[self.instructions[self.location+2]]
                    parameters //= 10
                    if parameters % 10 != 2:
                        v3 = self.instructions[self.location+3]
                    else:
                        v3 = relative_base + self.instructions[self.location+3]
                    if opcode == 1:
                        self.instructions[v3] = v1 + v2
                    else:
                        self.instructions[v3] = v1 * v2
                    self.location += 4
                elif opcode == 3:
                    # Write input
                    if parameters % 10 != 2:
                        self.instructions[self.instructions[self.location+1]] = self.input.get()
                    else:
                        self.instructions[relative_base + self.instructions[self.location+1]] = self.input.get()
                    self.location += 2
                elif opcode == 4:
                    # Print output
                    if parameters % 10 == 1:
                        yield( str(self.instructions[self.location+1]) )
                    elif parameters % 10 == 2:
                        yield( str(self.instructions[relative_base + self.instructions[self.location+1]]) )
                    else:
                        yield( str(self.instructions[self.instructions[self.location+1]]) )
                    self.location+=2
                elif opcode in [5, 6]:
                    # jumps
                    v1, v2 = 0, 0
                    if parameters % 10 == 1: 
                        v1 = self.instructions[self.location+1]
                    elif parameters % 10 == 2:
                        v1 = self.instructions[relative_base + self.instructions[self.location+1]]
                    else:
                        v1 = self.instructions[self.instructions[self.location+1]]
                    if v1 == 0 and opcode == 5 or v1 != 0 and opcode == 6:
                        self.location += 3
                        continue
                    parameters //= 10
                    if parameters % 10 == 1: 
                        v2 = self.instructions[self.location+2]
                    elif parameters % 10 == 2:
                        v2 = self.instructions[relative_base + self.instructions[self.location+2]]
                    else:
                        v2 = self.instructions[self.instructions[self.location+2]]
                    self.location = v2
                elif opcode in [7, 8]:
                    # Less than or equals
                    v1, v2 = 0, 0
                    if parameters % 10 == 1: 
                        v1 = self.instructions[self.location+1]
                    elif parameters % 10 == 2:
                        v1 = self.instructions[relative_base + self.instructions[self.location+1]]
                    else:
                        v1 = self.instructions[self.instructions[self.location+1]]
                    parameters //= 10
                    if parameters % 10 == 1: 
                        v2 = self.instructions[self.location+2]
                    elif parameters % 10 == 2:
                        v2 = self.instructions[relative_base + self.instructions[self.location+2]]
                    else:
                        v2 = self.instructions[self.instructions[self.location+2]]
                    parameters //= 10
                    if parameters % 10 != 2:
                        v3 = self.instructions[self.location+3]
                    else:
                        v3 = relative_base + self.instructions[self.location+3]
                    if v1 < v2 and opcode == 7 or v1 == v2 and opcode == 8:
                        self.instructions[v3] = 1
                    else:
                        self.instructions[v3] = 0
                    self.location += 4
                elif opcode == 9:
                    v1 = 0
                    if parameters % 10 == 1: 
                        v1 = self.instructions[self.location+1]
                    elif parameters % 10 == 2:
                        v1 = self.instructions[relative_base + self.instructions[self.location+1]]
                    else:
                        v1 = self.instructions[self.instructions[self.location+1]]
                    relative_base += v1
                    self.location += 2
                elif opcode == 99:
                    break
            except IndexError:
                self.instructions.append(0)


actions = {0: {(0, 1): (-1, 0), 
               (1, 0): (0, 1), 
               (-1, 0): (0, -1), 
               (0, -1): (1, 0)
              },
           1: {(-1, 0): (0, 1), 
               (0, 1): (1, 0), 
               (0, -1): (-1, 0), 
               (1, 0): (0, -1)
              }}

panels = defaultdict(int)
t = thruster(instructions)
loc = (0, 0)
direction = (0, 1)

color = panels[loc]
t.add_input(color)
gen = t.thrust()

while True:
    try:
        color = int(next(gen))
        action = int(next(gen))
        panels[loc] = color
        direction = actions[action][direction]
        loc = (loc[0]+direction[0], loc[1]+direction[1])
        t.add_input(panels[loc])
    except StopIteration:
        break

print(len(panels.keys()))

import math
with open('input.txt', 'r') as f:
    print(sum([math.floor(int(x)/3)-2 for x in f]))

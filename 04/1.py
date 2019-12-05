start = 248345
end = 746315
keys = 0

def is_increasing_and_adjecent(a):
    double = False
    high = 10
    while a != 0:
        value = a % 10
        if high < value:
            return False
        if high == value:
            double = True
        high = value
        a //= 10
    return double

while start < end:
    if is_increasing_and_adjecent(start):
        keys += 1
    start += 1

print(keys)

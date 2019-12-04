start = 248345
end = 746315
keys = 0

def is_increasing(a):
    high = 10
    while a != 0:
        value = a % 10
        if high < value:
            return False
        high = value
        a //= 10
    return True

def has_unique_double(a):
    a = list(str(a))
    if a[0] == a[1] and a[1] != a[2]:
        return True
    if a[-1] == a[-2] and a[-2] != a[-3]:
        return True
    for i in range(1, len(a)-2):
        if a[i-1] != a[i] and a[i] == a[i+1] and a[i+1] != a[i+2]:
            return True
    return False 
        
while start < end:
    if is_increasing(start) and has_unique_double(start):
        keys += 1
    start += 1

print(keys)

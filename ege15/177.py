def f(a):
    for x in range(1, 3000):
        f = ((x & 38 == 0) or (x & 57 == 0)) <= ((x & 11 != 0) <= (x & a == 0))
        if not f: return False
    return True

for a in range(1, 3000):
    if f(a):
        print(a)
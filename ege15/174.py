def f(a):
    for x in range(1, 1000):
        f = ((x & 28 == 0) or (x & 22 == 0)) <= ((x & 56 != 0) <= (x & a == 0))
        if not f: return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
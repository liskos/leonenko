def f(a):
    for x in range(1, 1000):
        f = (x & 56 != 0) <= ((x & 48 == 0) <= (x & a != 0))
        if not f: return False
    return True

for a in range(1, 250):
    if f(a):
        print(a)
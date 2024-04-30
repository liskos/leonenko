def f(a):
    for x in range(1, 1000):
        f = (x & a != 0) <= ((x & 30 == 0) <= (x & 20 != 0))
        if not f: return False
    return True

for a in range(1, 250):
    if f(a):
        print(a)
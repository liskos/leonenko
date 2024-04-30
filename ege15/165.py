def f(a):
    for x in range(1, 1000):
        f = ((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0) or ((x & a != 0) and (x & 39 == 0))
        if not f: return False
    return True

for a in range(1, 250):
    if f(a):
        print(a)
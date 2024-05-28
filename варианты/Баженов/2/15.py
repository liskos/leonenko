def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            ff = ((3*y + x) != 350) or (3*x > a) or (2*y > a)
            if not ff: return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)

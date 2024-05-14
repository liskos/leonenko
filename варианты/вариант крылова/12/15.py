def f(a):
    b = range(4, 18 + 1)
    c = range(12, 40 + 1)

    for x in range(1, 1000):
        f = (x in a) or ((x in b) == (x in c))
        if not f:
            return False
    return True

minimum = 99999
for x in range(1, 1000):
    for y in range(x, 1000):
        a = range(x,y)
        if f(a):
            minimum = min(minimum, len(a)-1)
print(minimum)

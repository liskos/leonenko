def f(a):
    p = range(6,17)
    q = range(30,51)
    for x in range(1, 1001):
        f = (not(x in a) or (x in q)) or (x in p)
        if not f:
            return False
    return True


m = 0
for i in range(1, 101):
    for g in range(i, 101):
        a = range(i,g)
        if f(a):
            m = max(m, len(a)-1)
print(m)
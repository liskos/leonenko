def f(a):
    P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    for x in range(1, 1001):
        f = (not((x in a)) or (x in P)) and ((x in Q) or not(x in a))
        if not f:
            return False
    return True


a = set()
for i in range(1, 1000):
    a.add(i)
    if not f(a):
        a.remove(i)
print(a)



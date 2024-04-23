p = range(25*10, 37*10+1)
q = range(32*10, 47*10+1)

def alg(a):
    for x in range(1, 1000):
        f = not((x in a) and not(x in p)) or (not(x in p) and (x in q))
        if not f:
            return False
    return True

m = 0
for x in range(1, 1000):
    for y in range(x, 1000):
        s = range(x, y)
        if alg(s):
            m = max(m, len(s) - 1)
            if len(s) - 1 == m:
                print(x/10,y/10, m)

p = range(5, 31)
q = range(14,24)


def alg(A):
    for x in range(1, 1000):
        f = not((x in p) == (x in q)) or not(x in A)
        if not f:
            return False
    return True

m = 0
for x in range(1, 300):
    for y in range(x, 300):
        s = range(x,y)
        if alg(s):
            m = max(m, len(s)-1)
print(m)
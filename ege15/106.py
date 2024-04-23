p = range(43,50)
q = range(44,54)
def alg(A):
    for x in range(1,1000):
        f = (not(x in A) or (x in p)) or (x in q)
        if not f:
            return False
    return True

m = 0
for x in range(1,1000):
    for y in range(x,1000):
        z = range(x,y)
        if alg(z):
            m = max(m, len(z) - 1)
print(m)

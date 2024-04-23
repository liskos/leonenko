p = range(44,50)
q = range(28,54)

def alg(A):
    for x in range(1, 1000):
        f = ((x in A) <= (x in p)) or (x in q)
        if not f:
            return False
    return True

m = 0
for x in range(1,1000):
    for y in range(x,1000):
        A = range(x,y)
        if alg(A):
            m = max(m, len(A)-1)
print(m)


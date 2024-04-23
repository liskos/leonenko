p = range(15,40)
q = range(44,58)

def alg(A):
    for x in range(1, 1000):
        f = (not(x in A) or (x in q)) or (x in q)
        if not f:
            return False
    return True

m = 0
for x in range(1,600):
    for y in range(x, 600):
        s = range(x,y)
        if alg(s):
            m = max(m, len(s)-1)
print(m)
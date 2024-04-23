p = {2,4,6,8,10,12,14,16, 18, 20}
q = {3,6,9,12,15,18,21,24,27,30}

def alg(a):
    for x in range(1, 200):
        f = (not(x in a) or not(x in p)) and ((x in q) or not(x in a))
        if not f:
             return False
    return True

a = set()
for x in range(1, 100):
    a.add(x)
    if not alg(a):
        a.remove(x)
print(a)


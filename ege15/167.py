p = {2,4,6,8,10,12,14,16,18,20}
q = {3,6,9,12,15,18,21,24,27,30}

def f(a):
    for x in range(1, 1000):
        f = ((x in p) <= (x in a)) or ((x not in a) <= (x not in q))
        if not f: return False
    return True

a = {a for a in range(1, 500)}
for A in range(1, 500):
    a.remove(A)
    if not f(a):
        a.add(A)
print(a)
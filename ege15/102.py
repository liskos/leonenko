y = {1,12}
z = {12,13,14,15,16}
def f(A):
    for x in range(1, 1000):
        f = not(not(x in A)) or (not(x in y) and not(x in z))
        if not f:
            return False
    return True

A = {a for a in range(1,1000)}
for a in range(1,1000):
    A.remove(a)
    if not f(A):
        A.add(a)
print(A)
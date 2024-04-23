y = {1,2,3,4,5,6}
z = {3,5,15}
def f(A):
    for x in range(1, 1000):
        f = not(not(x in A)) or (not(x in y) and (x in z)) or not(x in z)
        if not f:
            return False
    return True

A = {a for a in range(1,1000)}
for a in range(1,1000):
    A.remove(a)
    if not f(A):
        A.add(a)
print(A)
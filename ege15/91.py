y = {3,5,7,11,12,15}
z = {5,6,12,15}
def f(A):
    for x in range(1, 1000):
        f = ((x in y) <= (x in z)) or (x in A)
        if not f:
            return False
    return True

A = {a for a in range(1,1000)}
for a in range(1,1000):
    A.remove(a)
    if not f(A):
        A.add(a)
print(A)
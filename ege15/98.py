y = {2,4,8,12,16}
z = {3,6,7,15}
def f(A):
    for x in range(1, 1000):
        f = not(x in y) and not(x in z) or not(x in z) or (x in A)
        if not f:
            return False
    return True

A = {a for a in range(1,1000)}
for a in range(1,1000):
    A.remove(a)
    if not f(A):
        A.add(a)
print(A)
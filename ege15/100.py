y = {1,3,7}
z = {1,2,4,5,6}
def f(A):
    for x in range(1, 1000):
        f = not(not(x in A)) or not(x in y) or (not(x in z) and (x in y))
        if not f:
            return False
    return True

A = {a for a in range(1,1000)}
for a in range(1,1000):
    A.remove(a)
    if not f(A):
        A.add(a)
print(A)
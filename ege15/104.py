y = {3,6,9,12}
z = {1,2,3,4,5,6}
def f(A):
    for x in range(1, 1000):
        f = not(not(x in A) and (x in y)) or not(x in z)
        if not f:
            return False
    return True

A = {a for a in range(1,1000)}
for a in range(1,1000):
    A.remove(a)
    if not f(A):
        A.add(a)
print(A)
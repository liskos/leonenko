a = {2,4,6,8,10,12}
b = {3,6,9,12,15}

def f(A):
    for x in range(1, 1000):
        f = not(x in a) or (not(x in b)) <= (x in A)
        if not f:
            return False
    return True

A = [x for x in range(1, 100)]
for i in range(1, 100):
    A.remove(i)
    if not f(A):
        A.append(i)
print(A)
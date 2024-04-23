z = {1,2,3,4,5,6}
y = {3,6,9,12,15}

def f(A):
    for x in range(1, 1000):
        f = not(x in z) or ((not(x in y)) <= (x in A))
        if not f:
            return False
    return True

A = [a for a in range(1, 1000)]
for a in range(1,1000):
    A.remove(a)
    if not f(A):
        A.append(a)
print(len(A), A)
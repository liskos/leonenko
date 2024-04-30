def alg(a):
    for x in range(1, 1000):
        f = ((x % a != 0) and (x % 21 == 0)) <= (x % 14 != 0)
        if not f: return False
    return True

for A in range(1, 1000):
    if alg(A):
        print(A)
def alg(a):
    for x in range(1, 2000):
        f = (x % a == 0) or (x%28 != 0) or (x % 49 != 0)
        if not f:
            return False
    return True

for a in range(1, 2000):
    if alg(a):
        print(a)
def alg(a):
    for x in range(1, 100):
        f = not ((x % a != 0) and (x % 6 == 0)) or (x % 3 != 0)
        if not f:
            return False
    return True

for a in range(1, 100):
    if alg(a):
        print(a)
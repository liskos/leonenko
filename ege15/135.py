def f(a):
    for x in range(1, 1000):
        f = (x % a == 0) <= ((x % 14 == 0) and (x % 21 == 0))
        if not f:
            return False
    return True

for a in range(1, 100):
    if f(a):
        print(a)
def f(a):
    for x in range(1, 1000):
        f = (x % a == 0) <= ((x % 28 != 0) or (x % 42 == 0))
        if not f:
            return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
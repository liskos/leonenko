def f(a):
    for x in range(1, 1000):
        f = ( (x % a == 0) and (x % 50 != 0) ) <= ( (x % 18 != 0) or (x % 50 == 0) )
        if not f:
            return False
    return True

for a in range(1, 350):
    if f(a):
        print(a)
        break
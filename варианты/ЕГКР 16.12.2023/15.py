def f(a):
    for x in range(1, 10001):
        y = (x&a == 0) or not(x&37 == 0) or not(x&12==0)
        if not y:
            return False
    return True

for a in range(1, 10000):
    if f(a):
        print(a)
def f(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]

def alg(n):
    t = f(n)
    if (n%4==0):
        t+=t[-2:]
    else:
        h = f((n%4)*4)
        t+=h
    return int(t,3)

for i in range(1, 1000000):
    if alg(i) < 127:
        print(i, alg(i))
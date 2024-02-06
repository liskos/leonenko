def alg(n):
    if n % 3 == 0:
        n=n//3
    else:
        n=n-1
    if n % 5 == 0:
        n=n//5
    else:
        n=n-1
    if n % 11 == 0:
        n=n//11
    else:
        n=n-1
    return n

k=0
for i in range(2, 100000):
    if alg(i) == 8:
        print(alg(i))

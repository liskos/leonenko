def alg(n):
    if n % 3 == 0:
        n=n/3
    else:
        n=n-1
    if n % 7 == 0:
        n=n/7
    else:
        n=n-1
    if n % 11 == 0:
        n=n/11
    else:
        n=n-1
    return n

k=0
for i in range(2, 1000):
    if alg(i) == 6:
        k+=1
print(k)
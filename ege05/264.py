def alg(n):
    if n % 2 == 0:
        n=n/2
    else:
        n=n-1
    if n % 5 == 0:
        n=n/5
    else:
        n=n-1
    if n % 7 == 0:
        n=n/7
    else:
        n=n-1
    return n

k=0
for i in range(2, 1000):
    if alg(i) == 6:
        k+=1
print(k)
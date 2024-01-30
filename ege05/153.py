def alg(n):
    n = bin(n)[2:]
    if int(n[-1]) % 2 == 0:
        n=n+'01'
    else:
        n=n+'10'
    return int(n,2)

for n in range(1, 1000):
    if alg(n) > 130:
        print(alg(n))
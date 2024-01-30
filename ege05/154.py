def alg(x):
    n = bin(x)[2:]
    if x % 2 == 0:
        n=n+'01'
    else:
        n=n+'10'
    return int(n,2)

for n in range(1, 1000):
    if alg(n) > 73:
        print(n)
        break
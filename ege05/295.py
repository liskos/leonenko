def alg(n, m):
    n = bin(n)[2:]
    m = bin(m)[2:]
    sn = n.count('1') ** 2
    sm = m.count('1') ** 2
    return sn - sm

for n in range(1, 10000):
    for m in range(1, 10000):
        if alg(n,m) == 33:
            print(n+m)
            break
def alg(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    return (int(n, 2))

for n in range(1, 1000):
    if alg(n) < 125:
        print(alg(n))
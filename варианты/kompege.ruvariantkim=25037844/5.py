def alg(n):
    n = bin(n)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    return int(n, 2)

for i in range(1, 10000):
    if alg(i) > 60:
        print(alg(i))
        break

def alg(n):
    n = bin(n)[2:]
    if int(n[-1]) % 2 == 0:
        n = '10' + n + '1'
    else:
        n = '1' + n + '01'
    return int(n, 2)

for i in range(1, 100000):
    if alg(i) > 420:
        print(i)
        break
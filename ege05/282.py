def alg(n):
    n = bin(n)[2:]
    if int(n[-1]) % 2 == 0:
        n=n+bin(n.count('1'))[2:]
    else:
        n = '1' + n + '00'
    return int(n, 2)

for i in range(1, 1000000):
    if alg(i) > 215:
        print(i)
        break

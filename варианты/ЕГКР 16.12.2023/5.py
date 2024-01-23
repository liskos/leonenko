def alg(n):
    n = str(bin(n))[2:]
    if int(n[-1]) % 2 == 0:
        n = n + n[-2] + n[-1]
    else:
        n = '1' + n + '0'
    return int(n, 2)

for n in range(1,1000):
    if alg(n) < 100:
        print(n)
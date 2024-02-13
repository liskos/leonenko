def alg(n):
    n = bin(n)[2:]
    if int(n[-1]) % 2 == 0:
        n = n + '10'
    else:
        n = '1' + n + '01'
    return int(n, 2)

for i in range(1, 100000):
    if alg(i) > 516:
        print(i)
        break
def alg(n):
    n = bin(n)[2:]
    if n[-1] == '0':
        n = '10' + n
    else:
        n = '1' + n + '01'
    return int(n,2)

for n in range(1, 200):
    if alg(n) > 516:
        print(n)

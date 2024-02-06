def alg(n):
    n=bin(n)[2:]
    if int(n[-1]) == 1:
        n = '1' + n + '11'
    else:
        n = '11' + n + '00'
    return int(n,2)
for i in range(1, 1000):
    if alg(i) < 127:
        print(alg(i))
def alg(n):
    n=bin(n)[2:]
    if int(n[-1]) % 2 != 0:
        n = '1' + n + '0'
    else:
        n = '11' + n + '11'
    return int(n,2)

a=list()
for i in range(1, 1000):
    if alg(i) < 126:
        a.append(alg(i))
print(max(a))
def alg(n):
    n=bin(n)[2:]
    if int(n[-1]) == 1:
        n = '10' + n + '11'
    else:
        n = '1' + n + '00'
    return int(n,2)
a = list()
for i in range(1, 1000):
    if alg(i) > 1023:
        a.append(alg(i))
print(min(a))
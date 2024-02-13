def alg(n):
    n = bin(n)[2:]
    if int(n[-1]) % 2 == 0:
        n = '1' + n + '11'
    else:
        n = '11' + n + '0'
    return int(n, 2)

k=0
for i in range(1, 100000):
    if 500 <= alg(i) <= 1000:
        k+=1
print(k)
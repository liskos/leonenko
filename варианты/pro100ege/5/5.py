def alg(n):
    b = bin(n)[2:]
    if (n%3 == 0):
        b = b.replace('0', '11')
    else:
        b = b.replace('1', '10')
    return int(b,2)

a = list()

for n in range(1, 10000):
    if alg(n) <= 161:
        a.append(alg(n))
print(max(a))
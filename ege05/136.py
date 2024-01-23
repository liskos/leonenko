k = 0
def alg(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    return (int(n, 2))

a = []
for n in range(1, 100000):
    if 16 <= alg(n) <= 32:
        a.append(alg(n))
print(a)
print(32-16+1 - len(set(a)))


k = 0
def alg(n):
    n = bin(n)[2:]
    n += n[-1]
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    return (int(n, 2))

for n in range(1, 100):
    if alg(n) > 114:
        print(n)
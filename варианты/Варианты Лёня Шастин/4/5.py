def alg(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = '11' + n[2:] + '0'
    else:
        n = '10' + n[2:] + '1'
    return int(n,2)

s = set()
for n in range(1, 50):
    s.add(alg(n))
print(s)
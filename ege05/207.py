def alg(n):
    n=bin(n)[2:]
    n=n+f'{n.count('1') % 2}'
    n=n+f'{n.count('1') % 2}'
    return int(n,2)
a = set()
for i in range(1, 1000):
    if alg(i) < 100:
        a.add(alg(i))
print(len(a))
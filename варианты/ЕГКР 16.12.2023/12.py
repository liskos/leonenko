def alg(n):
    while ('333' in n) or ('555' in n):
        if '555' in n:
            n = n.replace('555', '3', 1)
        else:
            n = n.replace('333', '5', 1)
    return n

summ = []
for i in range(4, 10000):
    n = '3' + ('5' * i)
    summ.append(sum(map(int, alg(n))))
    if i % 100 == 0:
        print(i //100, max(summ))

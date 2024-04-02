def alg(n):
    while ('23' in n) or ('5333' in n) or ('33333' in n):
        if '23' in n:
            n = n.replace('23', '3', 1)
        if '5333' in n:
            n = n.replace('5333', '32', 1)
        if '33333' in n:
            n = n.replace('33333', '55', 1)
    return n

summi = []
for i in range(4,2000):
    n = ('3' * i) + '5'
    g = sum([int(x) for x in alg(n)]) # сумма измененной строки
    summi.append(g)
print(min(summi))
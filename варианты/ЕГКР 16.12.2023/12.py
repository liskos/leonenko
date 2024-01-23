n = ''
m = 0
summ = []
def alg(n):
    while ('333' in n) or ('555' in n):
        if '555' in n:
            n = n.replace('555', '3', 1)
        else:
            n = n.replace('333', '5', 1)
    return n

for i in range(4, 10000):
    n = '3' + ('5' * i)
    maximum = max(m, sum(map(int, alg(n))))
print(maximum)
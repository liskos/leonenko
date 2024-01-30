m=0
def alg(n):
    while ('57' in n) or ('877' in n) or ('777' in n):
        if '57' in n:
            n=n.replace('57','7',1)
        if '877' in n:
            n=n.replace('877','75',1)
        if '777' in n:
            n=n.replace('777','8',1)
    return n

for i in range(4,10000):
    n='5' + i*'7'
    m = max(m, sum(map(int, alg(n))))
print(m)
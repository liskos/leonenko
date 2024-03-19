def alg(n):
    while ( '25' in n ) or ( '355' in n  ) or ( '555' in n ):
        if '25' in n:
            n = n.replace('25', '5', 1)
        if '355' in n:
            n = n.replace('355', '52', 1)
        if '555' in n:
            n = n.replace('555', '3', 1)
    return n

for i in range(4, 30000):
    n = '3' + i * '5'
    if alg(n).count('5') == len(alg(n)):
        print(i)
        break
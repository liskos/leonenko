def alg(n):
    while ('12' in n) or ('3322' in n) or ('2222' in n):
        if '12' in n:
            n = n.replace('12', '33', 1)
        if '2222' in n:
            n = n.replace('2222', '1', 1)
        if '3322' in n:
            n = n.replace('3322', '21', 1)
    return sum([int(i) for i in n])

for i in range(4, 10000):
    n = '1' + ('2' * i)
    if alg(n) == 218:
        print(i)

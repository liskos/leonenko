def alg(n):
    while ('27' in n) or ('377' in n) or ('777' in n):
        if '27' in n:
            n = n.replace('27', '32', 1)
        if '377' in n:
            n = n.replace('377', '27', 1)
        if '777' in n:
            n = n.replace('777', '3', 1)
    return n

for n in range(210, 300):
    s = '3' + ('7' * n)
    a = [int(a) for a in alg(s)]
    if sum(a) % 15 == 0:
        print(n)
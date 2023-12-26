def f(n):
    while ('94' in n) or ('644' in n) or ('444' in n):
        if '94' in n:
            n = n.replace('94', '4', 1)
        if '644' in n:
            n = n.replace('644', '49', 1)
        if '444' in n:
            n = n.replace('444', '6', 1)
        return n


for n in range(4, 1000):
    s = '9' + '4' * n
    k = f(s).count('4')
    if n == 18 * k:
        print(n)


def alg(n):
    while ('>4' in n) or ('>5' in n) or ('>6' in n):
        if '>4' in n:
            n = n.replace('>4', '55>', 1)
        if '>5' in n:
            n = n.replace('>5', '5>4', 1)
        if '>6' in n:
            n = n.replace('>6', '4>5', 1)
    return n
for n in range(1, 1000):
    f = alg('>' + '4' * n + '5' * 25 + '6' * n)
    f = f.replace('>', '')
    a = len([x for x in f if int(x) % 2 == 0])
    b = len([x for x in f if int(x) % 2 != 0])
    if b == 10 * a:
        print(n)
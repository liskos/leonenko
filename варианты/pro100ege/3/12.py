def f(n):
    while '52' in n or '2222' in n or '1122' in n:
        if '52' in n:
            n = n.replace('52', '11')
        if '2222'  in n:
            n = n.replace('2222', '5')
        if '1122' in n:
            n = n.replace('1122', '25')
    return n

for i in range(4, 10000):
    s = '5' + '2' * i
    s2 = f(s)
    if sum(map(int, s2)) == 64:
        print(i)
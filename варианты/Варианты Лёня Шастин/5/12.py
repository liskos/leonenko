def alg(n):
    while ('72' in n) or ('522' in n) or ('2222' in n):
        if '72' in n:
            n = n.replace('72', '2', 1)
        if '522' in n:
            n = n.replace('522', '27', 1)
        if '2222' in n:
            n = n.replace('2222', '5', 1)
    return n
s = set()
for i in range(4, 10000):
    n = '5' + '2' * i
    x = [int(x) for x in alg(n)]
    if sum(x) == 22:
        s.add(i)
print(min(s))
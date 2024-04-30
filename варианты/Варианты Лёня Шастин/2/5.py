def schisl(n):
    s = ''
    while n > 0:
        s = s + str(n % 7)
        n = n // 7
    return s[::-1]


def alg(n):
    n = schisl(n)
    if n.count('2') % 2 == 0:
        n = n + '555'
    else:
        n = '1' + n
    return int(n, 7)

for n in range(1, 1000000):
    if alg(n) < 3799:
        print(n)
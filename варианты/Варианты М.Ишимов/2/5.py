def sis(n):
    s = ''
    while n > 0:
        s = s + str(n % 3)
        n = n // 3
    s = s[::-1]
    return s


def alg(n):
    s = sis(n)
    if n % 2 == 0:
        s = s.replace('1', '2')
        s = s + s[-2:]
    else:
        s = s + str(n % 3) + str(n % 3)
    return int(s, 3)

for n in range(1, 100000):
    if alg(n) <= 1165:
        print(n)
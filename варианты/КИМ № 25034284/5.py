def schisl(n):
    k=''
    while n > 0:
        if (n % 12 == 10):
            k+='A'
            n //= 12
        elif (n % 12 == 11):
            k+='B'
            n //= 12
        k+=str(n%12)
        n //= 12
    k = k[::-1]
    if k[0] == '0':
        k = k.replace('0', '', 1)
    return k


def alg(n):
    m='0'
    n = schisl(n)
    if int(n, 12) % 4 == 0:
        n = '2' + n + '64'
    else:
        for i in n:
            if int(i,12) > int(m, 12):
                m=i
        n=n+m
    return int(n, 12)

for n in range(1, 10000):
    if alg(n) > 1799:
        print(n, alg(n))

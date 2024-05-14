def schisl(n):
    s = ''
    while n > 0:
        s = s + str(n % 3)
        n = n // 3
    return s[::-1]

def alg(n):
    s = schisl(n)
    if n % 3 == 0:
        s = s + '02'
    else:
        s = '1' + s + '2'
    return int(s, 3)

a = []

for i in range(1, 10000):
    if alg(i) <= 167:
        a.append(alg(i))
print(max(a))
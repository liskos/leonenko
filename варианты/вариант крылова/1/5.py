def schisl(n):
    t = ''
    while n > 0:
        t = t + str(n % 4)
        n = n // 4
    t = t[::-1]
    return t

def alg(n):
    if n % 4 == 0:
        t = schisl(n) + schisl(n)[-2:]
    else:
        t = schisl(n) + schisl((n % 4) * 2)
    return int(t, 4)

s = set()
for i in range(1, 400):
    if alg(i) < 261:
        s.add(i)
print(max(s))
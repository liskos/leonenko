def schisl(n):
    s = ''
    while n > 0:
        s = s + str(n % 3)
        n = n // 3
    return s[::-1]
def alg(n):
    s = schisl(n)
    if n % 7 == 0:
        s = s + s[-2:]
    else:
        s = s + schisl((n % 7) * 3)
    return int(s,3)

s = set()
for i in range(1,1000):
    if alg(i) > 369:
        s.add(alg(i))
print(min(s))



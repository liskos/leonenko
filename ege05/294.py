def alg(n):
    s = [str(n) for n in str(n)]
    if n % 2 == 0:
        s.sort(reverse=True)
        return int(''.join(s)) // 2
    if n % 2 != 0:
        sorted(s)
        return int(''.join(s)) * 2

for i in range(1000, 10000):
    if alg(i) - i == 1:
        print(alg(i))
        break

def schisl(n):
    s = ''
    while n > 0:
        s = s + str(n % 3)
        n = n // 3
    return s[::-1]

def main(n):
    s = schisl(n)
    summ = sum([int(x) for x in schisl(n)])
    if summ % 4 == 0:
        s = '1' + s[:-2]
    else:
        s = s + schisl(summ % 4 * 3)
    return int(s, 3)

s = set()
for i in range(1, 100000):
    if main(i) > 353:
        s.add(main(i))
print(min(s))
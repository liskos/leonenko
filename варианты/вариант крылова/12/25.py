def deliteli(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    return sorted(s)

for i in range(800_000-1, 1, -1):
    if not deliteli(i):
        m = 0
    else:
        m = max(deliteli(i)) - min(deliteli(i))
    if (m != 0) and (m % 23 == 0):
        print(i, m)
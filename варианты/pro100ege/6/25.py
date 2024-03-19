def f(n):
    a = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return list(a)


for i in range(351, 994):
    a = f(i**2)
    if len(a) == 5:
        b = sorted(a)
        print(i**2, b[-2:])

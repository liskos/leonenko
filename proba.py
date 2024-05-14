def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(850000, 2_200_000):
    f = div(x)[-1] - div(x)[0]
    if f != 0 and f % 3 == 0:
        print(x, '|', f)
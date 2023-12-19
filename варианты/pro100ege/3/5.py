def f(n):
    n = str(n)
    a1 = int(n[0]) * int(n[1])
    a2 = int(n[1]) * int(n[2])
    m1 = min(a1,a2)
    m2 = max(a1,a2)
    return str(m1) + str(m2)

for i in range(100,1000):
    if f(i) == '621':
        print(i)

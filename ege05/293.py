def alg(n, m):
    n = [int(i) for i in str(n)]
    m = [int(i) for i in str(m)]
    p1=1
    p2=1
    for i in range(len(n)):
        if n[i] !=0 and n[i] % 2 == 0:
            p1=p1*n[i]
    for i in range(len(m)):
        if m[i] != 0 and m[i] % 2 == 0:
            p1 = p1 * m[i]
    for i in range(len(n)):
        if n[i] % 2 !=0:
            p2 = p2 * n[i]
    for i in range(len(m)):
        if m[i] % 2 != 0:
            p2=p2*m[i]
    return abs(p2-p1)

for m in range(1, 10000):
    if alg(120, m) == 29:
        print(m)
        break
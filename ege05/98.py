def alg(n):
    n = str(n)
    p1 = int(n[0]) * int(n[1])
    p2 = int(n[1]) * int(n[2])
    return str(min(p1, p2)) + str(max(p1,p2))

for n in range(100,1000):
    if alg(n) == '621':
        print(n)

def alg(n):
    n = str(n)
    s1 = int(n[0]) + int(n[2])
    s2 = int(n[1]) + int(n[3])
    return str(min(s1,s2)) + str(max(s1,s2))

for i in range(1000,10000):
    if alg(i) == '58':
        print(i)
        break

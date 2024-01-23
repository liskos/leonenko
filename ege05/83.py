def alg(n):
    n = str(n)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    return str(min(s1,s2)) + str(max(s1,s2))

for i in range(100,1000):
    if alg(i) == '1115':
        print(i)
        break

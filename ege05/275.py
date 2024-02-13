def alg(n):
    s1=0
    s2=0
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            s1+=int(n[i])
        if (i+1) % 2 == 0:
            s2+=int(n[i+1])
    if ('0' not in n) and ('2' not in n) and ('4' not in n) and ('6' not in n) and ('8' not in n):
        s1=0
    return abs(s2-s1)

for i in range(1, 1000000):
    if alg(i) == 29:
        print(i)

def alg(n):
    s=0
    for i in range(16):
        if i % 2 == 0:
            s += 2*int(str(n)[i]) % 10 + 2*int(str(n)[i]) // 10
        else:
            s+=int(str(n)[i])
    return s%10==0
print(alg(4096830803098323))
for i in range(1234567891011122, 1234567891011121 + 10000):
    if alg(i):
        print(str(i)[-8:])
        break
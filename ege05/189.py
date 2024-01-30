def alg(j):
    n=bin(j)[2:].zfill(8)
    n = [x for x in n]
    for i in range(7):
        while n[i] != '1':
            n[i] = '0'
    return int(n,2)
print(alg(211))


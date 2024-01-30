def alg(j):
    n=bin(j)[2:].zfill(8)
    n=n.replace('0','2').replace('1', '0').replace('2', '1')
    return int(n,2) + 1
print(alg(120))


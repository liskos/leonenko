def alg(j):
    n=bin(j-1)[2:].zfill(8)
    n=n.replace('0','2').replace('1', '0').replace('2', '1')
    return int(n,2)
print(alg(204))


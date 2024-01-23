def alg(n):
    n = bin(n)[2:]
    if (n.count('1') % 2 == 0):
        n+='1'
    else:
        n+='0'
    if (n.count('1') % 2 == 0):
        n += '1'
    else:
        n += '0'
    return n

for n in range(1,100):
    if int(alg(n),2) > 54:
        print(int(alg(n),2))
        break
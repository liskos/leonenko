def alg(n):
    n = bin(n)[2:]
    if (n.count('1') % 2 == 0):
        n+='0'
    else:
        n+='1'
    if (n.count('1') % 2 == 0):
        n+='0'
    else:
        n+='1'
    return n

for n in range(1,100):
    if int(alg(n),2) > 121:
        print(n)
        break
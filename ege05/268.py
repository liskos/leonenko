def alg(n):
    n=bin(n)[2:]
    if n.count('1') > n.count('0'):
        n+='1'
    else:
        n+='0'
    if n.count('1') > n.count('0'):
        n+='1'
    else:
        n+='0'
    return int(n, 2)
for i in range(1, 1000):
    if alg(i) < 57:
        print(alg(i))
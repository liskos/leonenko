def alg(n):
    n=bin(n)[2:]
    n=n+str(n.count('1')%2)
    if n.count('1') > n.count('0'):
        n+='0'
    else:
        n+='1'
    return int(n, 2)
a = set()
for i in range(1,1000):
    if 50 <= alg(i) <= 80:
        a.add(alg(i))
print(len(a))
def alg(n):
    s=''
    while n > 0:
       s+=str((n%6))
       n//=6
    s=s+s[-1]
    s = int(s,6)
    s = bin(s)[2:]
    s=s+s[-1]
    return int(s,2)
a=[]
for i in range(1, 10000):
    if alg(i) < 344:
        a.append(alg(i))
print(max(a))
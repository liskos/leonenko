def dv(n):
    s=''
    while n > 0:
        ost = n % 12
        if ost == 10:
            s+='A'
        elif ost == 11:
            s+='B'
        else:
            s+=str(ost)
        n//=12
    return s[::-1]
def alg(n):
    s=dv(n)
    if n % 4 == 0:
        s='2' + s + '64'
    else:
        s=s+max(s)
    return int(s,12)

a = []
print(alg(11),alg(12))
for i in range(1,10000):
    if alg(i) > 1799:
        a.append(alg(i))
print(min(a))
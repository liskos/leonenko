def alg(n):
    s=''
    while n > 0:
       s+=str(n%4)
       n=n//4
    s = s[::-1]
    if int(s[-1]) % 2 != 0:
        s='2' + s + '11'
    else:
        s='13' + s + '02'
    return int(s, 4)
a=list()
for i in range(1, 1000):
    if alg(i) > 1000:
        a.append(alg(i))
print(min(a))
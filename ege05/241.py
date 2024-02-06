def alg(i):
    n1=bin(i)[2:].zfill(8)
    n2=n1[::-1]
    f1 = int(n1, 2)
    f2 = int(n2, 2)
    return f1-f2
a=[]
for i in range(1, 256):
    if alg(i):
        a.append(alg(i))
print(max(a))

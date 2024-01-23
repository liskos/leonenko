k=0
def alg(n):
    n = str(n)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    return str(min(s1,s2)) + str(max(s1,s2))

for n in range(100,1000):
    if alg(n) == '1216':
        k+=1
print(k)

def alg(n):
    s1=sum([int(i) for i in str(n) if int(i)%2==0])
    s2=sum([int(i) for i in str(n)[::2]])
    return abs(s1-s2)

for i in range(1, 10000000000):
    if alg(i) == 28:
        print(i)
        break

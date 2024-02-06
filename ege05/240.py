def alg(n):
    s=''
    for i in str(n):
        i=bin(int(i))[2:].zfill(4)
        s+=i
    s = s.replace('0', '2').replace('1', '0').replace('2', '1')
    return int(s,2)

for n in range(1, 1000):
    if alg(n) == 151:
        print(n)

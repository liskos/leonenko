s=set()
def alg(j):
    n=bin(j)[2:]
    h = n[1:]
    n = n[0] + h.replace('0','2').replace('1','0').replace('2', '1')
    return j + int(n,2)

for i in range(1,1000):
    if alg(i) <= 123:
        print(i)
s = set()
def alg(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = '1' + n + '00'
    else:
        n = '11' + n
    return int(n,2 )

k=0
for i in range(1, 100000):
    if alg(i) >= 412:
        print(i)
        break
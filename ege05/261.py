def alg(n):
    n=bin(n)[2:]
    if n.count('0') > 0:
        n = n[:n.rfind('0')] + n[0] + n[1] + n[n.rfind('0')+1:]
    else:
        return False
    return int(n[::-1], 2)
k=0
for i in range(2, 1000):
    if alg(i) == 127:
        print(alg(i))
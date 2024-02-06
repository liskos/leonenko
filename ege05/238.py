def alg(n):
    n=str(n)
    n=n+n[-1]
    b = bin(int(n))[2:]
    if b.count('1') % 2 != 0:
        b+='1'
    else:
        b+='0'
    return int(b,2)

for i in range(1, 500):
    if alg(i) > 413:
        print(i)
        break
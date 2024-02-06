def alg(n):
    b = bin(n)[2:]
    if int(b[-1]) % 2 == 0:
        b+='1'
    else:
        b+='0'
    if int(b[-1]) % 2 == 0:
        b+='1'
    else:
        b+='0'
    return int(b,2)

for i in range(1, 10000):
    if alg(i) < 171:
        print(i)

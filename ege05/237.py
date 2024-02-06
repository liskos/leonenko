def alg(n):
    b = bin(n)[2:]
    if int(b[-1]) % 2 != 0:
        b+='0'
    else:
        b='1'+b
    if b.count('1') % 2 == 0:
        b+='1'
    else:
        b+='0'
    return int(b,2)

for i in range(1, 2000):
    if alg(i) > 228:
        print(i)
        break
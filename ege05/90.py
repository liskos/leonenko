def alg(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    return int(b, 2)




for i in range(1, 10000):
    if alg(i) > 108:
        print(i, alg(i))
        break
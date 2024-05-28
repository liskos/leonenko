def alg(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '11' + b[2:] + '10'
    else:
        b = b + b[:3]
    if int(b,2) % 2 == 0:
        b = b[:2] + b[3:]
    else:
        b = b[:4] + b[5:]
    return int(b,2)
k = 0
for n in range(10, 1001):
    if 800 <= alg(n) <= 1600:
        k = k + 1
print(k)

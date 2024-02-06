def alg(n):
    c=n//2
    h=hex(c)[2:]
    if n % 4 != 0:
        h='F' + h + 'A0'
    else:
        h='15' + h + 'C'
    return int(h, 16)
for i in range(1, 10000):
    if alg(i) < 65536:
        print(i)

def alg(n):
    old=bin(n)[2:].zfill(8)
    new = bin(n)[2:].zfill(8)
    new=bin(n)[2:].zfill(8).replace('0', '2').replace('1', '0').replace('2', '1')
    return int(new,2) - n

for n in range(256):
    if alg(n) == 99:
        print(n)
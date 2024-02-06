def alg(n):
    n=bin(n)[2:].zfill(8)
    a = [symbol for symbol in n]
    return int(a[0] + a[1] + a[6] + a[7], 2)

for n in range(1, 110):
    if alg(n) == 7:
        print(n)
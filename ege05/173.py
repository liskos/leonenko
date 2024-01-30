def alg(n):
    n=bin(n)[2:].zfill(8)
    a = [symbol for symbol in n]
    return int((a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6])[::-1], 2)

for n in range(1, 100):
    if n == alg(n):
        print(n)
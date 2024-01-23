k = 0
def alg(n):
    n = bin(n)[2:]
    if int(n[-1]) % 2 == 0:
        n = n + '00'
    else:
        n = n + '11'
    return (int(n, 2))

for n in range(1, 100):
    if alg(n) > 115:
        print(n)
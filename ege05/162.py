def alg(n):
    n=bin(n)[2:]
    R=n[::-1]
    while R[0] == '0':
        R = R[1:]
    return int(R,2)

for n in range(1,100):
    if alg(n) == 9:
        print(n)

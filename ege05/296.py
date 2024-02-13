def alg(n):
    n = str(n)[::-1]
    n = [int(i) for i in n]
    for i in 1,3,5,7,9,11,13,15:
        n[i] = n[i] * 2
        if str(n[i]) == 2:
            n[i] = sum(str(n[i]))
    if sum(n) % 10 == 0:
        return True
    else:
        return False

for i in range(1234567891011121, 1234567891011121 + 10000):
    if alg(i) == True:
        print(str(i)[-8:])
        break
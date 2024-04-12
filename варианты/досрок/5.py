def alg(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '01'
    else:
        b = '1' + b + '1'
    return int(b,2)

for i in range(1, 300):
    if alg(i) > 156:
        print(i)
        break
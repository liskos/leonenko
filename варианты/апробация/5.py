def alg(n):
    b = bin(n)[2:]
    if (n % 2 == 0):
        b = '10' + b
    else:
        b = '1' + b + '01'
    return int(b,2)
s = []
for i in range(1, 10000):
    if alg(i) > 516:
        s.append(i)
print(s, min(s),sep='\n')
print(alg(65))
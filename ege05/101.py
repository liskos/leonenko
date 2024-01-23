def alg(n):
    n1 = n % 4
    n2 = n % 2
    n3 = n % 3
    return str(n1) + str(n2) + str(n3)

for n in range(10,100):
    if alg(n) == '112':
        print(n)
        break
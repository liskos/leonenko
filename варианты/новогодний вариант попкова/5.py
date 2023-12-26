def f(n):
    b = bin(n)[2:]
    if n % 8 == 0:
        b = b + b[-2:]
    else:
        b = b + bin((n%8)*2)[2:]
    return int(b, 2)


for i in range(1, 1000):
    if f(i) > 3000:
        print(i)
        break
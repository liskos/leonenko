def alg(n):
    b=bin(n)[2:]
    if (n % 3 == 0):
        b = b + b[-3:]
    else:
        b=b + bin((n % 3) * 3)[2:]
    return int(b,2)
s = set()
for i in range(1, 1000):
    if alg(i) <= 170:
        s.add(alg(i))
print(max(s))
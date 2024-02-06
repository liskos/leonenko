def alg(n):
    b = bin(n)[2:]
    b = b + b[-2]
    b = b + b[1]
    return int(b,2)

k=0
for i in range(3,1000):
    if 150 <= alg(i) <= 250:
        k+=1
print(k)
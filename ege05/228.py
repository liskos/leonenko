def alg(n):
    b = bin(n)[2:]
    b = b + b[-2]
    b = b + b[1]
    return int(b,2)

for i in range(3,1000):
    if alg(i) <= 190:
        print(i)
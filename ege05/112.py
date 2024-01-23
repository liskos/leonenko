def alg(n):
    n = str(n)
    umn1 = int(n[0]) * int(n[1])
    umn2 = int(n[1]) * int(n[2])
    return str(max(int(umn1), int(umn2))) + str(min(int(umn1), int(umn2)))

for n in range(100,1000):
    if alg(n) == '123':
        print(n)
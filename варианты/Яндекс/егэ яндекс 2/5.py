def alg(n):
    if len(set(str(n))) < 4:
        return 10
    n = sorted([i for i in str(n)])
    s = int(n[0]) + int(n[3])
    u = int(n[1]) * int(n[2])
    answer = str(min(s,u)) + str(max(s,u))
    return int(answer)

for i in range(1000, 10000):
    if alg(i) > 85:
        print(i)
        break
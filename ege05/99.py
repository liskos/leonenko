def alg(n):
    n = str(n)
    s1 = int(n[0]) + int(n[2]) + int(n[4])
    s2 = int(n[1]) + int(n[3])
    return str(min(s1, s2)) + str(max(s1,s2))

for n in range(10000,99999):
    if alg(n) == '621':
        print(n)
        break
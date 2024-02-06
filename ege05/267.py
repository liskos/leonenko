def alg(n):
    n=bin(n)[2:]
    s = n[0] + n[1:].replace('0', '2').replace('1', '0').replace('2', '1')
    return int(n,2) + int(s,2)
for i in range(1, 1000, 2):
    if alg(i) > 99:
        print(i)
        break
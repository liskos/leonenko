def alg(n):
    while ('52' in n) or ('2222' in n) or ('1122' in n):
        if '52' in n:
            n = n.replace('52', '11', 1)
        if '2222' in n:
            n = n.replace('2222', '5', 1)
        if '1122' in n:
            n = n.replace('1122', '25', 1)
    return n

for n in range(4,10000):
    s='5' + ('2' * n)
    if str(sum(map(int, alg(s))))[-1] == '7':
        print(n)
        break
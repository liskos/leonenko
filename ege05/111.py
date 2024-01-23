def p(n):
    k = ""
    while n > 0:
        k = str(n % 12) + k
        n //= 12
    return k


def f(s):
    summ1 = int(s[0], 12) + int(s[2], 12)
    summ2 = int(s[1], 12) + int(s[3], 12)
    summ1, summ2 = max(summ1, summ2), min(summ1, summ2)
    answer = p(summ1) + p(summ2)
    return answer


print(f("441b"))
for n0 in '12456b':
    for n1 in '12456b':
        for n2 in '12456b':
            for n3 in '12456b':
                s = n0+n1+n2+n3
                if f(s) == "115":
                    print(s)

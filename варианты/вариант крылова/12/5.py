def alg(n):
    chisli = [int(i) for i in str(n)]
    umn = chisli[0] * chisli[1] * chisli[2]
    summ = sum(chisli)
    return str(max(umn, summ)) + str(min(umn, summ))

for n in range(100, 1000):
    if alg(n) == '24019':
        print(n)
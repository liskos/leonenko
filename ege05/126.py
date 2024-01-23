def alg(n):
    answer = []
    n = str(n)
    summ1 = int(n[0]) + int(n[1])
    summ2 = int(n[1]) + int(n[2])
    summ3 = int(n[2]) + int(n[3])
    answer.append(summ1)
    answer.append(summ2)
    answer.append(summ3)
    answer.sort()
    return str(answer[0]) + str(answer[1])


for n in range(1000,10000):
    if alg(n) == '1114':
        print(n)
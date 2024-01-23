def alg(n1, n2):
    numbers = []
    s1 = int(str(n1)[2]) + int(str(n2)[2])
    s2 = int(str(n1)[1]) + int(str(n2)[1])
    s3 = int(str(n1)[0]) + int(str(n2)[0])
    numbers.append(s1)
    numbers.append(s2)
    numbers.append(s3)
    numbers.sort()
    summ = str(numbers[0]) + str(numbers[1]) + str(numbers[2])
    return summ


for n1 in range(100, 1000):
    for n2 in range(100, 1000):
        if alg(n1, n2) == '71113' and (n1 == 497 or n2 == 497):
            print(n1, n2)
            break

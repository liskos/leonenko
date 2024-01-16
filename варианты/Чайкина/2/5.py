def R(N):
    s = ''
    while N > 0:
        s+=str((N%8))
        N = N // 8
    return s
summ = 0

for N in range(0,10000):
    for i in str(N):
        summ += int(i)

    if (summ % 2 == 0):
        answer = R(N) + str(N % 3)
    else:
        maximum = max(list(map(int, R(N))))
        answer = str(maximum) + R(N)
    print(N, int(answer,8))

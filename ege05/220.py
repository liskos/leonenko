


def alg(n):
    a = sorted([int(i) for i in str(n)])
    if a[0] != 0:
        minimum = str(a[0]) + str(a[1])
        maximum = str(a[2]) + str(a[1])
    elif a[1] != 0:
        minimum = str(a[1]) + str(a[0])
        maximum = str(a[2]) + str(a[1])
    else:
        minimum = str(a[2]) + '0'
        maximum = str(a[2]) + '0'
    return int(maximum) - int(minimum)


k=0
for i in range(700,801):
    if alg(i) == 80:
        k+=1
print(k)



a = []


def alg(n):
    for i in str(n):
        a.append(int(i))
        a.sort()
    if a[0] != 0:
        minimum = str(a[0]) + str(a[1])
        maximum = str(a[2]) + str(a[1])
    else:
        minimum = str(a[1]) + str(a[0])
        maximum = str(a[2]) + str(a[1])
    a.clear()
    return int(maximum) - int(minimum)
k=0
for i in range(500,601):
    if alg(i) == 10:
        k+=1
print(k)



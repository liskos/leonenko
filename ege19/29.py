def f(i,k):
    return (i+3,k), (i*2,k), (i,k+3), (i,k*2)

a = [[' '] * 200 for _ in range(200)]

for i in range(200):
    for k in range(200):
        if i + k >= 72:
            a[i][k] = '0'

for i in range(200):
    for k in range(200):
        if (a[i][k] == ' ') and any(a[m][q] == '0' for m,q in f(i,k)):
            a[i][k] = '1'

for i in range(200):
    for k in range(200):
        if (a[i][k] == ' ') and all(a[m][q] == '1' for m,q in f(i,k)):
            a[i][k] = '2'

for i in range(200):
    for k in range(200):
        if (a[i][k] == ' ') and any(a[m][q] == '2' for m,q in f(i,k)):
            a[i][k] = '3'

for i in range(200):
    for k in range(200):
        if (a[i][k] == ' ') and all(a[m][q] in '13' for m, q in f(i, k)):
            a[i][k] = '4'

for i in range(1,200):
    print(*a[i][1::], sep='\t')


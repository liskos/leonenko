def f(i,k):
    return (i+1,k), (i*2,k), (i,k+1), (i,k*2)

a = [[' '] * 200 for _ in range(200)]

for i in range(200):
    for k in range(200):
        if i + k >= 41:
            a[i][k] = '0'

for i in range(200):
    for k in range(200):
        if a[i][k] == ' ' and any(a[j][f] == '0' for j,f in f(i,k)):
            a[i][k] = '1'

for i in range(200):
    for k in range(200):
        if a[i][k] == ' ' and all(a[j][f] == '1' for j,f in f(i,k)):
            a[i][k] = '2'

for i in range(200):
    for k in range(200):
        if a[i][k] == ' ' and any(a[j][f] == '2' for j,f in f(i,k)):
            a[i][k] = '3'

for i in range(200):
    for k in range(200):
        if a[i][k] == ' ' and all(a[j][f] in '13' for j,f in f(i,k)):
            a[i][k] = '4'

for i in range(1, 200):
    print(*a[i][1::], sep='\t')


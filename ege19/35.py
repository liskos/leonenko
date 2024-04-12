def f(k,m):
    return (k+1,m), (k*2,m), (k,m+1), (k,m*2)

a = [[' '] * 200 for _ in range(200)]

for k in range(200):
    for m in range(200):
        if k + m >= 61:
            a[k][m] = '0'

for k in range(200):
    for m in range(200):
        if a[k][m] == ' ' and any(a[g][h] == '0' for g,h in f(k,m)):
            a[k][m] = '1'

for k in range(200):
    for m in range(200):
        if a[k][m] == ' ' and all(a[g][h] == '1' for g,h in f(k,m)):
            a[k][m] = '2'

for k in range(200):
    for m in range(200):
        if a[k][m] == ' ' and any(a[g][h] == '2' for g,h in f(k,m)):
            a[k][m] = '3'

for k in range(200):
    for m in range(200):
        if a[k][m] == ' ' and all(a[g][h] in '13' for g,h in f(k,m)):
            a[k][m] = '4'

for i in range(1, 200):
    print(*a[i][1::], sep ='\t')
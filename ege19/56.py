def f(i,k):
    return (i+1,k), (i*4,k), (i, k+1), (i,k*4)

a = [[' '] * 700 for _ in range(700)]

for i in range(700):
    for k in range(700):
        if i + k >= 105:
            a[i][k] = '0'

for i in range(700):
    for k in range(700):
        if a[i][k] == ' ' and any(a[m][h] == '0' for m,h in f(i,k)):
            a[i][k] = '1'

for i in range(700):
    for k in range(700):
        if a[i][k] == ' ' and all(a[m][h] == '1' for m,h in f(i,k)):
            a[i][k] = '2'

for i in range(700):
    for k in range(700):
        if a[i][k] == ' ' and any(a[m][h] == '2' for m,h in f(i,k)):
            a[i][k] = '3'

for i in range(700):
    for k in range(700):
        if a[i][k] == ' ' and all(a[m][h] in '13' for m,h in f(i,k)):
            a[i][k] = '4'

for i in range(1,700):
    print(*a[i][1::], sep='\t')
def f(i,k):
    return (k+1,i), (k*4,i), (k,i+1), (k,i*4)

a = [[' '] * 700 for i in range(700)]

for i in range(700):
    for k in range(700):
        if k + i >= 133:
            a[i][k] = '0'

for i in range(700):
    for k in range(700):
        if a[i][k] == ' ' and any(a[f][d] == '0' for f,d in f(i,k)):
            a[i][k] = '1'

for i in range(700):
    for k in range(700):
        if a[i][k] == ' ' and all(a[f][d] == '1' for f,d in f(i,k)):
            a[i][k] = '2'

for i in range(700):
    for k in range(700):
        if a[i][k] == ' ' and any(a[f][d] == '2' for f,d in f(i,k)):
            a[i][k] = '3'

for i in range(700):
    for k in range(700):
        if a[i][k] == ' ' and all(a[f][d] in '13' for f,d in f(i,k)):
            a[i][k] = '4'

for i in range(1,700):
    print(*a[i][1::], sep='\t')
def f(i,j):
    return (i+1,j),(i*2,j),(i,j+1),(i,j*2)

a = [[' '] * 200 for _ in range(200)]
for i in range(200):
    for j in range(200):
        if i + j >= 83:
            a[i][j] = '0'

for i in range(200):
    for j in range(200):
        if (a[i][j] == ' ') and any([a[k][m]=="0" for k,m in f(i,j)]):
            a[i][j] = '1'

for i in range(200):
    for j in range(200):
        if (a[i][j] == ' ') and all([a[k][m]=="1" for k,m in f(i,j)]):
            a[i][j] = '2'

for i in range(200):
    for j in range(200):
        if (a[i][j] == ' ') and any([a[k][m]=="2" for k,m in f(i,j)]):
            a[i][j] = '3'

for i in range(200):
    for j in range(200):
        if (a[i][j] == ' ') and all([a[k][m] in "13" for k,m in f(i,j)]):
            a[i][j] = '4'

for i in range(1, 200):
    print(*a[i][1::], sep='\t')

a = [[' '] * 3000 for _ in range(3000)]

def f(i,k):
    return (i+1,k), (i*2,k), (i,k+1), (i,k*2)

for i in range(1, 100):
    for k in range(1, 100):
        if i + k >= 59:
            a[i][k] = '0'

for i in range(59):
    for k in range(59):
        if a[i][k] == ' ' and any(a[h][j] == '0' for h,j in f(i,k)):
            a[i][k] = '1'

for i in range(59):
    for k in range(59):
        if a[i][k] == ' ' and all(a[h][j] == '1' for h,j in f(i,k)):
            a[i][k] = '2'

for i in range(59):
    for k in range(59):
        if a[i][k] == ' ' and any(a[h][j] == '2' for h,j in f(i,k)):
            a[i][k] = '3'

for i in range(59):
    for k in range(59):
        if a[i][k] == ' ' and all(a[h][j] in '13' for h,j in f(i,k)):
            a[i][k] = '4'

for i in range(1, 59):
    print(*a[i][1::], sep = '\t')

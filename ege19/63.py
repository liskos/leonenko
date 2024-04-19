def f(a,b):
    return (a+1,b), (a,b+1), (a*2,b), (a,b*3)

a = [[' '] * 800 for _ in range(800)]

for i in range(800):
    for k in range(800):
        if i + k >= 30:
            a[i][k] = '0'

for i in range(800):
    for k in range(800):
        if a[i][k] == ' ' and any(a[s][f] == '0' for s,f in f(i,k)):
            a[i][k] = '1'

for i in range(800):
    for k in range(800):
        if a[i][k] == ' ' and all(a[s][f] == '1' for s,f in f(i,k)):
            a[i][k] = '2'

for i in range(800):
    for k in range(800):
        if a[i][k] == ' ' and any(a[s][f] == '2' for s,f in f(i,k)):
            a[i][k] = '3'

for i in range(800):
    for k in range(800):
        if a[i][k] == ' ' and all(a[s][f] in '13' for s,f in f(i,k)):
            a[i][k] = '4'

for i in range(1, 800):
    print(*a[i][1::], sep='\t')
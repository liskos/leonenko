a = [[' '] * 1000 for _ in range(1000)]

def alg(f,k):
    return (f+1,k), (f*2,k), (f,k+1), (f,k*2)

for i in range(600):
    for q in range(600):
        if i + q >= 59:
            a[i][q] = '0'

for u in range(59):
    for i in range(59):
        if a[u][i] == ' ' and any(a[m][q] == '0' for m,q in alg(u,i)):
            a[u][i] = '1'

for u in range(59):
    for i in range(59):
        if a[u][i] == ' ' and all(a[m][q] == '1'  for m,q in alg(u,i)):
            a[u][i] = '2'

for u in range(59):
    for i in range(59):
        if a[u][i] == ' ' and any(a[m][q] == '2' for m,q in alg(u,i)):
            a[u][i] = '3'

for u in range(59):
    for i in range(59):
        if a[u][i] == ' ' and all(a[m][q] in '13' for m,q in alg(u,i)):
            a[u][i] = '4'

for i in range(1, 59):
    print(*a[i][1::], sep='\t')
a = [[' '] * 400 for _ in range(400)]
def alg(j,l):
    return (j+1,l), (j*2,l), (j,l+1), (j,l*2)


for j in range(1, 400):
    for l in range(1, 400):
        if j + l >= 123:
            a[j][l] = '0'

for j in range(123):
    for l in range(123):
        if a[j][l] == ' ' and any(a[f][k] == '0' for f,k in alg(j,l)):
            a[j][l] = '1'

for j in range(123):
    for l in range(123):
        if a[j][l] == ' ' and all(a[f][k] == '1' for f,k in alg(j,l)):
            a[j][l] = '2'

for j in range(123):
    for l in range(123):
        if a[j][l] == ' ' and any(a[f][k] == '2' for f,k in alg(j,l)):
            a[j][l] = '3'

for j in range(123):
    for l in range(123):
        if a[j][l] == ' ' and all(a[f][k] in '13' for f,k in alg(j,l)):
            a[j][l] = '4'

for j in range(1, 123):
    print(*a[j][1:], sep='\t')



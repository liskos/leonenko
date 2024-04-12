def f(i):
    a = []
    if (i+1) % 2 != 0:
        a.append(i+1)
    if (i*3) % 2 != 0:
        a.append(i*3)
    if (i+3) % 2 != 0:
        a.append(i+3)
    return a

a = [' '] * 200

for i in range(200):
    if i >= 51:
        a[i] = '0'

for i in range(60):
    if a[i] == ' ' and any(a[j] == '0' for j in f(i)):
        a[i] = '1'

for i in range(60):
    if a[i] == ' ' and all(a[j] == '1' for j in f(i)):
        a[i] = '2'

for i in range(60):
    if a[i] == ' ' and any(a[j] == '2' for j in f(i)):
        a[i] = '3'

for i in range(60):
    if a[i] == ' ' and all(a[j] in '13' for j in f(i)):
        a[i] = '4'

print(*a[1::], sep='\t')

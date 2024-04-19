def f(i):
    a = []
    if i % 2 == 0:
        a.append(i//2)
    else:
        a.append(i-2)
    if i % 3 == 0:
        a.append(i//3)
    else:
        a.append(i-3)
    return a

a = [' '] * 200
a[1] = '0'

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

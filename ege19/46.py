def f(i):
    return i+2, i*3

a = [' '] * 200

for i in range(200):
    if i >= 45 and i <= 112:
        a[i] = '0'
    if i > 112:
        a[i] = '-1'

for i in range(45):
    if a[i] == ' ' and any(a[j] == '0' for j in f(i)):
        a[i] = '1'

for i in range(45):
    if a[i] == ' ' and all(a[j] == '1' or a[j] == '-1' for j in f(i)):
        a[i] = '2'

for i in range(45):
    if a[i] == ' ' and any(a[j] == '2' for j in f(i)):
        a[i] = '3'

for i in range(45):
    if a[i] == ' ' and all(a[j] in '13' or a[j] == '-1' for j in f(i)):
        a[i] = '4'

print(*a[1::], sep='\t')

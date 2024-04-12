def f(i):
    return i+2, i*3

a = [' '] * 200

for i in range(200):
    if i >= 45:
        a[i] = '0'

for i in range(200):
    if a[i] == ' ' and any(a[m] == '0' for m in f(i)):
        a[i] = '1'

for i in range(200):
    if a[i] == ' ' and all(a[m] == '1' for m in f(i)):
        a[i] = '2'

for i in range(200):
    if a[i] == ' ' and any(a[m] == '2' for m in f(i)):
        a[i] = '3'

for i in range(200):
    if a[i] == ' ' and all(a[m] in '13' for m in f(i)):
        a[i] = '4'

print(*a[1::], sep='\t')
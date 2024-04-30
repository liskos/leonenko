a = [' '] * 30000

def alg(n):
    return (n-7), (int(n/3))

for k in range(120):
    if k < 117:
        a[k] = '0'

for k in range(20000):
    if a[k] == ' ' and any(a[x] == '0' for x in alg(k)):
        a[k] = '1'

for k in range(20000):
    if a[k] == ' ' and all(a[x] == '1' for x in alg(k)):
        a[k] = '2'

for k in range(20000):
    if a[k] == ' ' and any(a[x] == '2' for x in alg(k)):
        a[k] = '3'

for k in range(20000):
    if a[k] == ' ' and all(a[x] in '13' for x in alg(k)):
        a[k] = '4'

print(*a[1::], sep='\t')
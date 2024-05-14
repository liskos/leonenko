a = [' '] * 20000
def alg(n):
    return (n+1), (n*2)

for x in range(10000):
    if x >= 2022:
        a[x] = '0'

for x in range(2022):
    if a[x] == ' ' and any(a[i] == '0' for i in alg(x)):
        a[x] = '1'

for x in range(2022):
    if a[x] == ' ' and all(a[i] == '1' for i in alg(x)):
        a[x] = '2'

for x in range(2022):
    if a[x] == ' ' and any(a[i] == '2' for i in alg(x)):
        a[x] = '3'

for x in range(2022):
    if a[x] == ' ' and all(a[i] in '13' for i in alg(x)):
        a[x] = '4'

print(*a[1::], sep='\t')
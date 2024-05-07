f = [int(f) for f in open('17.txt')]
minimum = min([x for x in f if x % 19 == 0]) # 114

a = []
for i in range(9999):
    if (f[i] % minimum == 0) or (f[i+1] % minimum == 0):
        a.append(f[i] + f[i+1])
print(len(a), max(a))
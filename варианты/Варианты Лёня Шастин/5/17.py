a = [int(x) for x in open('17.txt')]

minimim = min([x for x in a if abs(x) % 100 == 25])  ** 2 # -88625
s = []
for i in range(6677):
    y = [len(str(abs(z))) == 4 for z in (a[i], a[i + 1], a[i + 2])]
    if (a[i] * a[i + 1] * a[i + 2] <= minimim) and (y.count(True) >= 2):
        s.append(a[i] * a[i + 1] * a[i + 2])
print(len(s), max(s))
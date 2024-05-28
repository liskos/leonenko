a = [int(s) for s in open('17.txt')]
maximum = max([int(s) for s in open('17.txt') if int(s) % 613 == 0]) # 9195
b = []
for i in range(len(a)-2):
    z = a[i:i+3]
    zz = [x for x in z if str(abs(x))[0] == '7']
    if len(zz) <= 2 and sum(z) > maximum:
        b.append(z[0] * z[1] * z[2])
print(len(b), max(b))
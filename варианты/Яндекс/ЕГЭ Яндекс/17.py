a = [int(x) for x in open('17.txt')]
print(a)
k = len(a)
b = []
for i in range(2, k - 3):
    s1 = a[i - 2] + a[i - 1]
    s2 = a[i] + a[i + 1]
    s3 = a[i + 2] + a[i + 3]
    if s1 > 0 and s2 > 0 and s3 > 0 and s2 > s1 and s2 > s3:
        b.append(a[i] * a[i + 1])
print(len(b), min(b))

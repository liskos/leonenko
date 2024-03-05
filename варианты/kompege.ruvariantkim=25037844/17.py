a = [int(x) for x in open('17.txt')]
k = 0
s = []
for i in range(1, 5000):
    if abs(a[i]) % 5 == 0 and abs(a[i]) % 3 != 0 and abs(a[i+1]) % 5 == 0 and abs(a[i+1]) % 3 != 0:
        k+=1
        if a[i] + a[i+1] > 0:
            s.append(a[i] + a[i+1])
print(k, min(s))
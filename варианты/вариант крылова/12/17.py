a = [int(a) for a in open('17.txt')]
b = []
for i in range(4999):
    if abs(a[i]) % 5 == 0  and  abs(a[i+1]) % 5 == 0:
        b.append(a[i] + a[i+1])
print(len(b), min(b))
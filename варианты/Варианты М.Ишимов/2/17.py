import sys
a = [int(x) for x in open('17.txt')]
maximum = 0
for i in range(1, 6667):
    if str(a[i])[-1] == '3' and a[i] > maximum:
        maximum = a[i]
k = 0
summa = []
for i in range(1, 6665):
    if ((a[i] % 2 != 0) + (a[i+1] % 2 != 0) + (a[i+2] % 2 != 0)) == 1 and a[i] + a[i+1] + a[i+2] >= maximum:
        k+=1
        summ = a[i] + a[i+1] + a[i+2]
        summa.append(summ)
print(k, sum(summa))


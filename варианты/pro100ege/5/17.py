a = [int(x) for x in open('17.txt')]
maximum = []
for i in range(1,4997):
    leni = set()
    leni.add(abs(a[i]) % 10)
    leni.add(abs(a[i+1]) % 10)
    leni.add(abs(a[i+2]) % 10)
    leni.add(abs(a[i+3]) % 10)
    if len(leni) == 1:
        summ = a[i] + a[i+1] + a[i+2] + a[i+3]
        maximum.append(summ)
A = max(maximum)
maximum_dvuznah = []
for i in range(1, 5000):
    if 10 <= a[i] <= 99:
       maximum_dvuznah.append(a[i])
dvuznah = max(maximum_dvuznah)

l=0
u=0
k=0
for i in range(1,4996):
    if a[i] < A:
        l+=1
    if a[i+1] < A:
        l+=1
    if a[i+2] < A:
        l+=1
    if a[i+3] < A:
        l+=1
    if a[i+4] < A:
        l+=1
    if (a[i] + a[i+1] + a[i+2] + a[i+3] + a[i+4]) % dvuznah == 0:
        u+=1
    if l == 1 and u == 1:
        k+=1
print(k)
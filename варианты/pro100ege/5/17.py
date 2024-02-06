a = [int(x) for x in open('17.txt')]
maximum = -50000
for i in range(0,4997):
    if str(a[i])[-1] == str(a[i+1])[-1] == str(a[i+2])[-1] == str(a[i+3])[-1]:
        maximum = max(maximum, a[i] + a[i+1] + a[i+2] + a[i+3])
maximum_dvuznah = []
for i in range(0, 5000):
    if 10 <= a[i] <= 99:
       maximum_dvuznah.append(a[i])
dvuznah = max(maximum_dvuznah)

b = []
for i in range(0,4996):
    ss = a[i:i+5]
    if len([j for j in ss if j < maximum]) == 1 and sum(ss) % dvuznah == 0:
        b.append(sum(ss))
print(len(b), min(b))


a = [int(x) for x in open('17.txt')]
minn = min([int(x) for x in open('17.txt') if (-99 <= int(x) <= -10) or (10 <= int(x) <= 99)])
maxx = max([int(x) for x in open('17.txt') if 1000 <= int(x) <= 9999 if int(x) % 10 == 1])
k = 0
m = []
for i in range(1, 4998):
    if ((a[i] > minn**2) + (a[i+1] > minn**2) + (a[i+2] > minn**2)) == 2 and ((abs(a[i]) * abs(a[i+1]) * abs(a[i+2])) % maxx == 0):
        k+=1
        m.append(abs(a[i]) + abs(a[i + 1]) + abs(a[i + 2]))
print(k, max(m))
f = open('24.txt').readline()
f = f.replace('R', 'Q').replace('W', 'Q')
f = f.replace('2', '1').replace('4', '1')
t = f[0]
m = 0
for i in f[1:]:
    if t[-1] == i:
        t = i
    else:
        t = t + i
        m = max(m, len(t))
print(m)
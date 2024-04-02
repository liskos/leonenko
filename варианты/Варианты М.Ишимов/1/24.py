f = open('24.txt').readline()
f = f.replace('A', '1').replace('B', '1').replace('C','1').replace('D', '1')
f = f.split('1')
m = 0
for i in range(782505):
    m = max(m, len(f[i]))
print(m)
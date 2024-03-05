f = open('24.txt').readline()
s = []
k = 1
for i in range(len(f)-1):
    if int(f[i]) < int(f[i+1]) or int(f[i]) == int(f[i+1]):
        k = k + 1
        s.append(k)
    else:
        k = 1
print(max(s))
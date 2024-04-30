f = open('24.txt').readline()
t = ''
m = 0
print(len(f))
print("@" in f)
f = f.replace("INFINITY", "@")
print(len(f))
for i in range(len(f)):
    t += f[i]
    while t.count('@') > 1000:
        t = t[1:]
    if t.count('@') == 1000:
        m = max(m, len(t))
    if i % 100000 == 0:
        print(i // 100000, "%")

print(m)
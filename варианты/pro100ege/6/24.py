f = open('24.txt').readline()
t = ''
m = 0
for i in f:
    t = t + i
    while 'XZZY' in t:
        t = t[1:]
    m = max(m, len(t))
    print(t)
print(m)
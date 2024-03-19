f = open('24.txt').readline()
f = f.replace('XZZY', '1')
s = f.split('1')
for i in range(len(s)):
    s[i] = len(s[i])
print(max(s))

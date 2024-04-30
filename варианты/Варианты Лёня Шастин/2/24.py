f = open('24.txt').readline()
s = ''
a = set()
for i in f:
    s = s + i
    if 'INFINITY' in s:
        s =
print(max(a))
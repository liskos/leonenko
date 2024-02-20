import sys
sys.stdin = open('24.txt')
s = input()
m = 0
t = ''
for i in s:
    t = t + i
    while t.count('Y') > 150:
        t = t[1:]
    m = max(m, len(t))
print(m)
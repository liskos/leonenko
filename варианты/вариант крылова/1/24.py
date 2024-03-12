import sys
sys.stdin = open('24.txt')
a = input()
t = ''
m = 10**10

for i in a:
    t = t + i
    while t.count('A') > 2024:
        t = t[1:]
    if t.count('A') == 2024:
        m = min(m, len(t))
        print(m)
print(m)

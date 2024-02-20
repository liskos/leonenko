def f(i):
    return i[1]


import sys
sys.stdin = open('26.txt')
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
b = a[:]
t = 0
c = []
while len(b) > 0:
    b = sorted(b, key=f)
    t = b[0][1]
    c.append(b[0])
    b.pop(0)
    x = b[:]
    b = [i for i in b if i[0] >= t ]

print(c)
print(len(c))
print(x)
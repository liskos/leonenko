import sys
sys.stdin = open('24.txt')
a = input()
k = 0
g = []
i = 0
while a[i] != '+' and a[i+1] != '+':
    k = k + 1
    i = i + 1
else:
    g.append(k)
    k = 0
print(g)
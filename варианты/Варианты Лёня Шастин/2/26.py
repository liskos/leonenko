import sys
sys.stdin = open("26_11681.txt")

n, k = map(int, input().split())
a = []
for _ in range(n):
    c,s = map(int, input().split())
    a.append([c,s,c*s/100])
a = sorted(a, key=lambda x: x[2], reverse=True)
s = 0
b = []
for i in range(0, k):
    s = s + (a[i][0] - a[i][2])

for i in range(k,n):
    s = s + a[i][0]

print(s)
print(a[k][2])
for i in a:
    if i[2] == a[k][2]:
       b.append(i[0])
print(min(b))
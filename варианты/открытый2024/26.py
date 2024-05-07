import sys
sys.stdin = open('26.txt')
n = int(input())
a = [int(input()) for _ in range(n)]
a = sorted(a, reverse=True)
b = [a[0]]
z = [x for x in a if b[-1] - x >= 4]
while z:
    b.append(z[0])
    z = [x for x in a if b[-1] - x >= 4]
print(len(b), b[-1])
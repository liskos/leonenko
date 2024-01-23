import sys
sys.stdin = open('17.txt')

a = [int(input()) for _ in range(6721)]
m = max([x for x in a if abs(x) % 10 == 3])
b = [a[i] + a[i+1] + a[i+2] for i in range(6719) if a[i] + a[i+1] + a[i+2] <= m and (abs(a[i]) % 10 == 3 or abs(a[i+1]) % 10 == 3 or abs(a[i+2]) % 10 == 3)]
print(len(b), max(b))
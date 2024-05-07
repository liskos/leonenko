import sys
sys.stdin = open('1_27_A.txt')
n = int(input())
a = [int(input()) for _ in range(n)]
b = []
for i in range(n): # i - мобильный пункт подготовки
    s = 0
    for g in range(n): # g - номер пункта питания, куда нужно привезти
        s = s + min(abs(i-g), n-abs(g-i)) * a[g]
    b.append(s)
print(min(b))
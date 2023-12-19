import sys
sys.stdin = open('17_11887.txt')
a = [int(input()) for i in range(6664)]
print(a)
b = max([i for i in a if str(i)[-2:] == '68'])
print(b)
k=0
g = []
for i in range(0, 6661):
    c = [a[i], a[i+1], a[i+2], a[i+3]]
    d = [x for x in c if 10<= abs(x) <= 99]
    if (len(d) == 1 or len(d) == 4) and sum(c) >= b:
        k+=1
        g.append(sum(c))
print(k, max(g))

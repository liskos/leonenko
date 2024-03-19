import sys
sys.stdin = open('17.txt')
a = [int(input()) for _ in range(10000)]
m221 = max([x for x in a if abs(x) % 1000 == 221])
b = []
for i in range(9998):
    t = a[i:i+3]
    h = [str(i)[-2] for i in t if abs(i) >=10 and int(str(i)[-2]) % 2 != 0]
    k = [i for i in t if 10 <= i <= 99]
    if len(h) == 2 and len(k) <= 2 and sum(t) > m221:
        b.append(sum(t))
print(len(b), min(b))
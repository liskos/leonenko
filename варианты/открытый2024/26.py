import sys
sys.stdin = open('26.txt')
t = []
k = 0
for i in range(1, 10001):
    s = input()
    t.append(s)
t = sorted(t, reverse=True)
q = []
for i in range(10000):
    q.append(t[i])
    if q[0] - t[i+1] >= 4:
        k = k + 1
        q.pop()
        q.append(t[i+1])
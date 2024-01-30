import sys
sys.stdin = open('17.txt')
g = [int(input()) for _ in range(6679)]
m=[]
for i in g:
    if abs(i) % 100 == 50:
        m.append(i)
maximum = max(m)
h=[]
for i in range(6677):
    if len(set(g[i:i+3])) == 3 and (len(str(abs(g[i]))) == 5) and (len(str(abs(g[i+1]))) == 5) and (len(str(abs(g[i+2]))) == 5) and sum(g[i:i+3]) <= maximum:
        h.append(sum(g[i:i+3]))
print(len(h), max(h))
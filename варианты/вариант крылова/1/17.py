import sys
a = [int(x) for x in open('17.txt')]
k = 0
g = []
for i in range(1, 6798):
    if ( len(str(a[i])) == 2 ) + ( len(str(a[i+1])) == 2 ) + ( len(str(a[i+2])) == 2 ) == 1 and (a[i] + a[i+1] + a[i+2] < 125):
        k = k + 1
        g.append(a[i] + a[i+1] + a[i+2])
print(k, max(g))
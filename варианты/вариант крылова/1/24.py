a = open('24.txt').readline()
i = 0
A = 0
g = []
while A < 2024:
    if a[i] == 'A':
        A = A + 1
    i = i + 1
    if A == 2024:
        a = a[i+1:]
        A = 0
        g.append(i)
        i = 0
print(g)
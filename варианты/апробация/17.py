s = [int(i) for i in open('17.txt')]
minimum = min([int(i) for i in open('17.txt') if int(i) % 19 == 0])
a = []
for i in range(9999):
    if (s[i] % minimum == 0) or (s[i+1] % minimum == 0):
        a.append(s[i] + s[i+1])
print(len(a), max(a))
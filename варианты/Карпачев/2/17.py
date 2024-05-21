a = [int(s) for s in open('17.txt')]
minimum = min([int(s) for s in open('17.txt') if (10 <= int(s) <= 99) and int(s[0]) > int(s[1])]) # 52
h = []
for i in range(len(a)-1):
    if (int(str(a[i])[-2:]) == minimum) or (int(str(a[i+1])[-2:]) == minimum):
        h.append(a[i]**2 + a[i+1]**2)
print(len(h), min(h))
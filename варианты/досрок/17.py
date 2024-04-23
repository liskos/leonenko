s = [int(s) for s in open('17.txt')]
maximum = max([x for x in s if x%19==0]) # 89737
summ = []
for i in range(9999):
    if (s[i] > maximum) or (s[i+1] > maximum):
        summ.append(s[i] + s[i+1])
print(len(summ), max(summ))
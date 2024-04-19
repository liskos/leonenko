m = 0
p = range(6, 17)
q = range(30, 51)
for i in range(1, 101):
    for g in range(i, 101):
        a = range(i,g)
        if all([(not (x in a) or (x in q)) or (x in p) for x in range(1, 1001)]):
            m = max(m, len(a)-1)
print(m)
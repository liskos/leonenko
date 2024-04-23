p = range(10,41)
q = range(30,51)

m = 0
for i in range(1, 100):
    for g in range(i,100):
        a = range(i,g)
        if all((not(x in a) or (x in q)) or (x in p) for x in range(1, 1000)):
            m = max(m, len(a))
print(m)
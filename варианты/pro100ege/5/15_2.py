a = set()
P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
for i in range(1, 1000):
    a.add(i)
    f = all([(not ((x in a)) or (x in P)) and ((x in Q) or not (x in a)) for x in range(1, 1001)])
    if not f:
        a.remove(i)
print(a)

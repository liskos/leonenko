a = set()
a.add(1)

for _ in range(15):
    b = set()
    for i in a:
        b.add(i + 10)
        b.add(i-5)
    a = b.copy()
print(len(a))
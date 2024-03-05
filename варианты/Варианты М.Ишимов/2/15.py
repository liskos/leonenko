s = set()
for A in range(1, 1000):
    if all((not (2 * x < 2 * A + 3 * y) or (y < 5) or (y >= 18) or (x < 87)) for x in range(1, 1000) for y in range(1,1000)):
        s.add(A)
print(max(s))
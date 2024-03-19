for A in range(1, 10000):
    if all((99 != y + 2 * x) or (A < x) or (A < y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)


for x in range(1, 10000):
    for A in range(1, 10000):
        f = all([(not (120 <= x <= 130) or not (x % 7 == 0)) or (A > 2 * x) for x in range(1, 10000)])
        if f:
            print(A)
            break

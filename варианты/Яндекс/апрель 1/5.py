def f(N):
    t = sum([int(x) for x in str(N)])
    n = str(N)
    a = sorted([t%int(n[0]), t%int(n[1]), t%int(n[2]), t%int(n[3])], reverse=True)
    return a[0] * 1000 + a[1] * 100 + a[2] * 10 + a[3]

print(f(5219))
for N in range(1000, 10000):
    if '0' in str(N):
        continue
    if f(N) > 2000:
        print(N)
        break
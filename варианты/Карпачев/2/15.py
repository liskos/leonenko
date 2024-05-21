def f(a):
    b = range(123*k, 163*k+1)
    e = range(145*k, 786*k+1)
    for x in range(1, 1000*k):
        ff = not(x in b) or ((x in e) or (x in a) or not(x in b))
        if not ff: return False
    return True

k = 10
m = 99999999
s1, s2 = 0, 0
for a1 in range(120*k, 150*k):
    for a2 in range(a1, 150*k):
        a = range(a1,a2)
        if f(a) and a2-a1 < m:
            m = a2-a1
            s2 = a2
            s1 = a1
print(m/10)
print(s1/k, s2/k)
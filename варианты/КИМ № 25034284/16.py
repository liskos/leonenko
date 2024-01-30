import sys

sys.setrecursionlimit(5000)

def f(n):
    global ff, gg
    if n in ff:
        return ff[n]
    if n < 10:
        ff[n] = n
        return n
    x = g(f(n-1)%10) + f(g(n%10)-1) - f(n-3)
    ff[n] = x
    return x


def g(n):
    global ff, gg
    if n in gg:
        return gg[n]
    if n < 10:
        gg[n] = -n
        return -n
    x = f(g(n-1)%10) + g(f(n-1)-1) + g(n-2)
    gg[n] = x
    return x

gg = dict()
ff = dict()
print(f(1111)+g(1111))
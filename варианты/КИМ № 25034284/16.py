import sys
sys.setrecursionlimit(5000)
def f(n):
    if n < 10:
        return n
    return g(f(n-1)%10) + f(g(n%10)-1) - f(n-3)

def g(n):
    if n < 10:
        return -n
    return f(g(n-1)%10) + g(f(n-1)-1) + g(n-2)
print(f(1111)+g(1111))
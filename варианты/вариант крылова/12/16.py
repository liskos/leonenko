import sys, functools
sys.setrecursionlimit(5000)
@functools.lru_cache(None)
def f(n):
    if n == 1: return 1
    if n == 2: return 2
    if n > 2: return n*(n-1) + f(n-1) + f(n-2)
print(f(2023) - f(2021) - (2 * f(2020)) - f(2019))

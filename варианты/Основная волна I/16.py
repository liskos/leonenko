from functools import lru_cache
import sys
sys.setrecursionlimit(15000)
def f(n):
    if n < 11:
        return n
    if n >= 11:
        return n + f(n-1)
print(f(2024)-f(2021))
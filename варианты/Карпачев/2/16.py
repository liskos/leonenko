import functools

@functools.lru_cache(None)
def f(n):
    if 0 <= n <= 2: return n
    if n > 2: return f(n-1) + 2 * f(n-2)

print(f(15)**2 - 2 * f(13) * f(15) + f(13)**2)
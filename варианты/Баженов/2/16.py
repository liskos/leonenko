from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 2: return n
    if n >=2 and n % 3 == 0: return f(n-1)+2*f(n-2)
    if n >= 2 and n % 3 != 0: return f(n-3)+3*f(n-1)-2
print(f(50), '|', sum([int(i) for i in str(f(50))]))
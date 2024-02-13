import sys
from functools import lru_cache
sys.setrecursionlimit(100000000)
@lru_cache(None)
def alg(n):
    k=0
    n = str(n)
    for i in range(len(n)+1):
        k+=i
    k = bin(k)[2:]
    if k.count('1') % 2 == 0:
        k = '1' + k + '00'
    else:
        k = '10' + k + '1'
    return int(k,2)
k=0
for i in range(100000000, 999999999):
    if alg(i) == 21:
        k+=1
print(k)
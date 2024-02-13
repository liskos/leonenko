from fnmatch import *
from functools import lru_cache
@lru_cache(None)
def f():
  for i in range(2*10**8, 0, -1):
    if fnmatch(str(i), '?2*4*0') and not fnmatch(str(i), '1*7*') and (i%42==0):
      return (i, '|', i/42)
print(f())
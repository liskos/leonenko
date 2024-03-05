from fnmatch import *
k = 0
for i in range(0, 10**11, 466963):
    if fnmatch(str(i), '?9?38*6?') and (i % 2 == 0) and (i % 466963) == 0:
        print(i, i / 466963)


from itertools import permutations
k = 0
for x in set(permutations('СОВЕСТЬ')):
    s = ''.join(x)
    for u in 'СВТ':
        s = s.replace(u, 'С')
    for h in 'ОЕЬ':
        s = s.replace(h, 'Г')
    if not('СС' in s and 'ГГ' in s):
        k = k+ 1
print(k)
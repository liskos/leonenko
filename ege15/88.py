def f(a):
    b = {2,4,6,8,10,12}
    c = {3,6,9,12,15}
    for x in range(1, 101):
        f = not(x in b) or not((x in c) and not(x in a)) or not(x in b)
        if not f:
            return False
    return True


a = {i for i in range(1, 101)}
for i in range(1, 101):
    a.remove(i)
    if not f(a):
        a.add(i)
print(a)
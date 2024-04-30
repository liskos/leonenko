p = {2,4,6,8,10,12,14,16,18,20}
q = {5,10,15,20,25,30,35,40,45,50}
def f(a):
    for x in range(1, 1000):
        f = ((x in a) <= (x in p)) or ((x not in q) <= (x not in a))
        if not f:
            return False
    return True

a = set()
for i in range(1, 1000):
    a.add(i)
    if not f(a):
        a.remove(i)
print(len(a))

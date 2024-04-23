p = range(5*100, 30*100+1)
q = range(14*100,23*100+1)


def alg(A):
    for x in range(-100, 1000):
        f = not((x in p) == (x in q)) or not(x in A)
        if not f:
            return False
    return True


print(alg(range(5*100, 13*100+99)))
print(len(range(5*100, 13*100+99))/100)
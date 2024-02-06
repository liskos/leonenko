def f(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    elif a == 11 or a == 12:
        return 0
    return f(a+1,b) + f(a*2,b) + f(a**2,b)

print(f(2,10) * f(10,40))
def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a < b:
        return f(a+2,b) + f(a*3,b)
print(f(2**2, 64))
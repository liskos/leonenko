def f(a,b):
    if a > b: return False
    if a == b: return True
    if a < b: return f(a+1,b) + f(a+2,b) + f(a*2,b)
print(f(4, 11) * f(11, 13) * f(13, 15))
def f(a,b):
    if a > b: return False
    if a == b: return True
    if a < b: return f(a+2,b) + f(a+10,b)

print(f(7, 71))
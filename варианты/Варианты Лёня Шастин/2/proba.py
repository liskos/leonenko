def f(a,b):
    if a == b or a == 13: return True
    if a > b: return False
    if a < b: return f(a+1,b) + f(a+2,b)
print(f(4,14))


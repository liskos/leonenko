def f(x,y):
    if x > y: return False
    if x == y: return True
    if x < y: return f(x+1,y) + f(x+2,y) + f(x*2,y)
print(f(4,11) * f(11, 13) * f(13, 15))
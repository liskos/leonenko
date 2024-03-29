def delenie(x, y):
    if x % y == 0:
        return True
    return False

for A in range(1, 50000):
    if all( (delenie(x, 15) and not(delenie(x, 10))) <= (A < (x+50)) for x in range(1, 1000)):
        print(A)
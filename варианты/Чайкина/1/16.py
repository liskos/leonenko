def H(x):
    if x < 3: return 1
    return 2*x - 1 + H(x - 2)
print(H(3033))
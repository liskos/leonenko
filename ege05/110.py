k = 0
def alg(x):
    number1 = x % 2
    number2 = x % 3
    number3 = x % 5
    number = str(number1) + str(number2) + str(number3)
    return number

for x in range(10, 100):
    if alg(x) == '122':
        k+=1
print(k)
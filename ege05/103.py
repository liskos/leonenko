def alg(x):
    number1 = x % 4
    number2 = x % 2
    number3 = x % 5
    number = str(number1) + str(number2) + str(number3)
    return number

for x in range(10, 100):
    if alg(x) == '313':
        print(x)
        break
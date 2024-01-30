k=0
def alg(i):
    k=oct(i)[2:]
    return k
for i in range(int("1000000",8), int('10000000',8)):
    if ( alg(i).count('0') + alg(i).count('2') + alg(i).count('4') + alg(i).count('6') ) == 2 and (('17' not in alg(i)) and ('37' not in alg(i)) and ('57' not in alg(i)) and ('77' not in alg(i)) and ('71' not in alg(i)) and ('73' not in alg(i)) and ('75' not in alg(i))) == True:
        k+=1
print(k)
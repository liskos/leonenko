k=0
def alg(i):
    k=''
    while i > 0:
        k+=str(i%8)
        i//=8
    return k[::-1]
for i in range(1000000, 10000000):
    if ( alg(i).count('0') + alg(i).count('2') + alg(i).count('4') + alg(i).count('6') ) == 2 and (('17' not in alg(i)) and ('37' not in alg(i)) and ('57' not in alg(i)) and ('77' not in alg(i)) and ('71' not in alg(i)) and ('73' not in alg(i)) and ('75' not in alg(i))) == True:
        k+=1
print(k)
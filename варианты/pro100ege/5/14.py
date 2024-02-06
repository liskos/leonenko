f = (3*3125**9) + (2*625**8) - (4*625**7) + (3 * 125**6) - (2*25**5) -2024
def alg(f):
    s=''
    while f > 0:
       if (f % 25 == 10):
           s+='A'
       elif (f % 25 == 11):
           s+='B'
       elif (f % 25 == 12):
           s+='C'
       elif (f % 25 == 13):
           s+='D'
       elif (f % 25 == 14):
           s+='E'
       elif (f % 25 == 15):
           s+='F'
       elif (f % 25 == 16):
           s+='G'
       elif (f % 25 == 17):
           s+='H'
       elif (f % 25 == 18):
           s+='I'
       elif (f % 25 == 19):
           s+='J'
       elif (f % 25 == 20):
           s+='K'
       elif (f % 25 == 21):
           s+='L'
       elif (f % 25 == 22):
           s+='M'
       elif (f % 25 == 23):
           s+='N'
       elif (f % 25 == 24):
           s+='O'
       elif (f % 25 == 25):
           s+='P'
       s+=str(f%25)
       f//=25
    return s

print(alg(f).count('0'))
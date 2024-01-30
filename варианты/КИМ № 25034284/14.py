def alg(n,x):
    k=''
    k = k.split()
       if int(k) % 31 == 0:
           return x
       return False

for x in '0123456789ABCDEFGHIJKLMNOPQRSTU':
    n = f'931{x}964' + f'4{x}51{x}1' + f'2861{x}637'
    print(alg(n,x))



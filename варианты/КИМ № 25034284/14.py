for x in '0123456789ABCDEFGHIJKLMNOPQRSTUV':
    n1= f'931{x}964'
    n2=f'4{x}51{x}1'
    n3=f'2861{x}637'
    s=int(n1,32) + int(n2,32) + int(n3,32)
    if s % 31 == 0:
        print(s//31)
        break




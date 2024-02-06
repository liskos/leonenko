def alg(n):
    n=str(n)
    s1=0
    if n.count('0') > 0 or n.count('2') > 0 or n.count('4') > 0 or n.count('6') > 0 or n.count('8') > 0:
        for i in str(n):
            if int(i) % 2 == 0:
                s1+=int(i)
    else:
        s1=0
    
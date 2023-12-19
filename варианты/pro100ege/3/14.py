for x in '0123456789AB':
    a1 = '9A87' + x + '21'
    a2 = '2' + x + '68'
    a3 = '1' + x +'2F4'
    s = int(a1, 12) + int(a2,14) - int(a3, 16)
    if s % 3 == 0:
        print(x, s//3)
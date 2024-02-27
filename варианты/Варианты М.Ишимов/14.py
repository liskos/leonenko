
for x in '012345679ABCDEFGIJKLMNOPQR':
    s1 = f'27{x}98876'
    s2 = f'26{x}51'
    s3 = f'15{x}47'
    s4 = f'62{x}5'
    if (int(s1,26) + int(s2, 26) + int(s3,26) + int(s4,26)) % 25 == 0:
        print(x, (int(s1,26) + int(s2, 26) + int(s3,26) + int(s4,26)) / 25)
        break

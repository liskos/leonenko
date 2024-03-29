s = set()
for x in 'D':
    s1 = f'71{x}264'
    s2 = f'4{x}51{x}1'
    s3 = f'21{x}637'
    print((int(s1,18) + int(s2,18) + int(s3,18)) / 17)

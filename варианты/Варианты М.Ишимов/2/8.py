k = 0
for s1 in '0123456789ABCDEFG':
    for s2 in '0123456789ABCDEFG':
        for s3 in '0123456789ABCDEFG':
            for s4 in '0123456789ABCDEFG':
                for s5 in '0123456789ABCDEFG':
                    s = s1 + s2 + s3 + s4 + s5
                    if s1 != '0' and s.count('1') <= 2 and ('31' not in s) and ('51' not in s) and ('71' not in s) and ('91' not in s) and ('B1' not in s) and ('D1' not in s) and ('F1' not in s) and ('11' not in s) and ('13' not in s) and ('15' not in s) and ('17' not in s) and ('19' not in s) and ('1B' not in s) and ('1D' not in s) and ('1F' not in s):
                        k = k + 1
print(k)
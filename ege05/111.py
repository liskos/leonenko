for n0 in '12456B':
    for n1 in '12456B':
        for n2 in '12456B':
            for n3 in '12456B':
                number = n0+n1+n2+n3
                summ1 = int(n0, 20) + int(n2, 20)
                summ2 = int(n1, 20) + int(n3, 20)
                answer = max(summ1,summ2) + min(summ1,summ2)
                if answer == 115:
                    print(number)

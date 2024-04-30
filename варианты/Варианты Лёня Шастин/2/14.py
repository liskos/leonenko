for x in '0123456789ABCDEFGHIJKLMNOPQ':
    f = f'17{x}35' + f'{x}742M' + f'{int(x,27)**3}'
    if int(f,27) % 23 == 0:
        print(x, int(f,27) // 23)
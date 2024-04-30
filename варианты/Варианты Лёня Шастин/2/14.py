for x in '123456789ABCDEFGHIJKLMNOPQ':
    f = int(f'17{x}35', 27) + int(f'{x}742M', 27) + int(x,27)**3
    if f % 23 == 0:
        print(x, f // 23)
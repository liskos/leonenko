from ipaddress import *
for x in '10000000', '11000000', '11100000', '11110000', '11111000', '11111100', '11111110', '11111111':
    net = ip_network(f'51.50.135.169/{int('11111111',2)}.{int('11111111',2)}.{int('11111111',2)}.{int(x, 2)}', 0)  # IP адресс
    seti = str(net.network_address).split('.') # адрес сети
    ipaddress = [int(x) for x in seti] # элементы адреса сети в типе int
    if sum(ipaddress) == 404:
        print(int(x,2))
        break

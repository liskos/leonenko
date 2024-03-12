for x in '0123456789abcdefghijklm':
    f = f'1{x}1{x}1{x}1{x}1' + f'20{x}24' + f'1{x}235'

x = 7
print( (int(f'1{x}1{x}1{x}1{x}1', 23) + int(f'20{x}24', 23) + int(f'1{x}235', 23)) / 22)
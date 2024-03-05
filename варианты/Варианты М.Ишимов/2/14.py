for x in '0123456789abcdefghij':
    a = all([(int(f'5{y}4{x}{y}4HJ4', 20) + int(f'4{y}6B{y}{x}1', 20)) % 15 == 0 for y in '0123456789abcdefghij'])
    if a:
        print(x)
y = 8
x = 'h'
print((int(f'5{y}4{x}{y}4HJ4', 20) + int(f'4{y}6B{y}{x}1', 20)))
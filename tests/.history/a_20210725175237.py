def conversion():
    global binaryOrDecimal 
    binaryOrDeceimal = input('''Which way are you trying to convert?
    A: Binary to Decimal
    B: Decimal to Binary
    ''')

conversion()

if binaryOrDecimal == 'a' or 'A':
    print('test')
elif binaryOrDecimal == 'b' or 'B':
    print('test2')
else:
    print('invalid argument, please try again')
    conversion()
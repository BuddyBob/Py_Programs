def conversion():
    global binaryOrDecimal 
    binaryOrDecimal = input('''Which way are you trying to convert?
    A: Binary to Decimal
    B: Decimal to Binary
    ''').lower()

conversion()
if (binaryOrDecimal in 'a' or 'A':
    print('test')
elif binaryOrDecimal == 'b' or 'B':
    print('test2')
else:
    print('invalid argument, please try again')
    conversion()
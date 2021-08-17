num = (input('Enter a number: '))
num = num.split(' ')
if num[1] == '+':
    print(int(num[0])+int(num[2]))
if num[1] == '/':
    print(int(num[0])/int(num[2]))
if num[1] == '-':
    print(int(num[0])-int(num[2]))
if num[1] == '*':
    print(int(num[0])*int(num[2]))




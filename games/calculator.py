num1 = float(input("Enter a number: "))
op = (input("Enter an operation: "))
num2 = float(input("Enter another number: "))
if op == "*":   
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "^":
    print(num1 ** num2)
else:
    print("error, you did not enter a supported operation")




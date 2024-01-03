# question3

number1 = int(input("enter your first number: "))
v = input("for add enter '+' for subtraction enter '-'. ")
number2 = int(input("enter your second number: "))

if v == "-":
    print(number1 - number2)
elif v == "+":
    print(number1 + number2)
else:
    print("please try again...")

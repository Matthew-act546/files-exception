print("Enter 2 number this program will divide it")

while True:
    num1 = input("Enter the first number here: ")
    if num1 == 'q':
        break
    num2 = input("Enter the second number here: ")
    if num2 == 'q':
        break
    try:
        answer = int(num1) / int(num2)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)    
while True:
    operator = input("choose tool (+, -, *, /) or type 'exit' to stop: ")

    if operator == 'exit':
        print("Calculator stopped.")
        break

    if operator not in ['+', '-', '*', '/']:
        print("Oops... wrong operator!")
        continue

    number1 = int(input("write 1-st number: "))
    number2 = int(input("write 2-th number: "))

    if operator == '+':
        print("Result:", number1 + number2)
    elif operator == '-':
        print("Result:", number1 - number2)
    elif operator == '*':
        print("Result:", number1 * number2)
    elif operator == '/':
        if number2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", number1 / number2)
history = []

while True:
    a = float(input("write a number:"))
    b = float(input("write b number:"))
    
    operator = input("choose, +, -, ×, ÷, P, exit, history:")
    
    if operator == '+':
        result = a + b
        print(result)
        history.append(f"{a} + {b} = {result}")
    elif operator == '-':
        result = a - b
        print(result)
        history.append(f"{a} - {b} = {result}")
    elif operator == '×':
        result = a * b
        print(result)
        history.append(f"{a} × {b} = {result}")
    elif operator == '÷':
        if b != 0: 
            result = a / b
            print(result)
            history.append(f"{a} / {b} = {result}")
        else:
            print("cannot divide by zero")
    elif operator == 'exit':
        break
    elif operator == 'history':
        print(history)
    elif operator == 'P':
        n = float(input("write n number"))
        result = (a + b) * n
        print(result)
        history.append(f"({a} + {b}) × {n} = {result}")
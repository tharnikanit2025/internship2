def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        if operator == "+":
            print("Result:", a + b)
        elif operator == "-":
            print("Result:", a - b)
        elif operator == "*":
            print("Result:", a * b)
        elif operator == "/":
            if b == 0:
                print("Error: Cannot divide by zero!")
            else:
                print("Result:", a / b)
        else:
            print("Invalid operator!")
    except ValueError:
        print("Error: Please enter valid numbers!")
    except OverflowError:
        print("Error: Number is too large!")
calculator()
number1 = float(input("Enter the first number:"))

number2 = float(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

match operation: 
    case "+":
        result = number1 + number2
        print(f"The result is {result}")

    case "-":
        result = number1 - number2
        print(f"The result is {result}")

    case "*":
        result = number1 * number2
        print(f"The result is {result}")

    case "/":
        if number2 !=0:
            result = number1 / number2
            print(f"the result is{result}")

        else:
            print("Cannot divide by zero.")
    case _:
        print("invalid operation")
        
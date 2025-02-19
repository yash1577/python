# design a simple calculator using a match case 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
    
    # Input operation from the user
operation = input("Select an operation (+, -, *, /): ")

    
match operation:
        case '+':
            result = num1 + num2
            print("the sum is",result)
        case '-':
            result = num1 - num2
            print("the substraction56 is",result)
        case '*':
            result = num1 * num2
            print("the multiplication is",result)
        case '/':
            if num2 != 0:
                result = num1 / num2
                print("the division is",result)
            else:print("Error: Division by zero is not allowed.")
    

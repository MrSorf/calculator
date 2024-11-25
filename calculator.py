def calculator(operation):
    print("Welcome to my simple calculator!")
    operation = (input("Please select an operation( +, -, *, /): "))
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if operation == '+':
        result = num1 + num2
        print(f"The result for {num1} + {num2} is {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result for {num1} - {num2} is {result}")
    elif operation == '*':
        result = num1 * num2
        print (f"The result for {num1} * {num2} is {result}")
    elif operation == '/':
        if num2 != 0: 
            result = num1 / num2 
            print(f"The result for {num1} / {num2} is {result}")
        else:
                print("Error: Number cannot be divisible by 0")
    else:
         print("Invalid operation, please try again")

calculator(2)
    

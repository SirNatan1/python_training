def calculate():
    # Define the function 'calculate'
    
    operation = input("Please type in the math operation you would like to complete (+, -, *, /): ")
    # Get the user's input for the operator (+, -, *, /)
    
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    # Get the user's input for the first and second numbers

    if operation == '+':
        print("The answer is: " + str(number_1 + number_2))
    elif operation == '-':
        print("The answer is: " + str(number_1 - number_2))
    elif operation == '*':
        print("The answer is: " + str(number_1 * number_2))
    elif operation == '/':
        print("The answer is: " + str(number_1 / number_2))
    # Check the operator input and perform the corresponding calculation
    # Convert the result to a string and print it
    
    else:
        print("You have entered an invalid operator, please run the program again.")
    # If the operator input is invalid, print an error message
    
calculate()
# Call the function 'calculate'

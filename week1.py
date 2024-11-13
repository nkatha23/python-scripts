# Function to perform the requested operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Main program
def main():
    # Get user input for numbers and operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the calculation and print the result
        result = calculate(num1, num2, operation)
        print(f"{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the main program
if __name__ == "__main__":
    main()

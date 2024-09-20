def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    print("Welcome to the Python Calculator")
    print("Enter 'exit' to quit the Calculator")

    while True:
        operation = input("\nEnter operation (+, -, *, /): ")

        if operation == 'exit':
            print ("Goodbye!")
            break

        if operation in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input. Please eneter numeric values.")
                continue
            if operation == "+":
                print(f"{num1} + {num2}") = {add(num1,num2)}

            elif operation == '-':
                print(f"{num1} - {num2}") = {substract(num1,num2)}

            elif operation == '*':
                print(f"{num1} * {num2}") = {multiply(num1,num2)}

            elif operation == '/':
                print(f"{num1} / {num2}") = {divide(num1,num2)}

    else:
        print("Error: Unsupported operation. Please use one of +, -, *, /.")

if __name__ == "__main__":
    calculator()
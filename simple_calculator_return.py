def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation"

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Choose operation (add/subtract/multiply/divide): ")

result = calculator(num1, num2, op)
print("Result:", result)

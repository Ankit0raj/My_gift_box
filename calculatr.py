def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero is undefined."
    return x % y

# Display options to the user
print("Welcome to the Calculator!")
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Modulus (%)")

# Get user's choice
choice = input("Enter choice (1/2/3/4/5): ")

# Check if the choice is valid
if choice in ('1', '2', '3', '4', '5'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculation based on user choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", modulus(num1, num2))
else:
    print("Invalid input. Please select a valid operation.")

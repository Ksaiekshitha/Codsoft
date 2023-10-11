
def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a,b):
    if b == 0:
        return "please enter valid numbers"
    return a / b
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    result = "Invalid choice"
print(f"Result: {result}")

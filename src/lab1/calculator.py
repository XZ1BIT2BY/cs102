from future import absolute_import

OPERATION_ADDITION = "1"
OPERATION_SUBTRACTION = "2"
OPERATION_MULTIPLICATION = "3"
OPERATION_DIVISION = "4"


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: division by zero"


print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the operation number (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == OPERATION_ADDITION:
    print(num1, "+", num2, "=", addition(num1, num2))
elif choice == OPERATION_SUBTRACTION:
    print(num1, "-", num2, "=", subtraction(num1, num2))
elif choice == OPERATION_MULTIPLICATION:
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif choice == OPERATION_DIVISION:
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Error: invalid operation input")

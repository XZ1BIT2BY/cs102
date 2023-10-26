import random

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: division by zero"

def generate_random_numbers():
    return random.uniform(-100, 100), random.uniform(-100, 100)

def test_calculator():
    for _ in range(10):  # Run 10 random tests
        num1, num2 = generate_random_numbers()
        
        # Test addition
        assert addition(num1, num2) == num1 + num2

        # Test subtraction
        assert subtraction(num1, num2) == num1 - num2

        # Test multiplication
        assert multiplication(num1, num2) == num1 * num2

        # Test division
        if num2 != 0:
            assert division(num1, num2) == num1 / num2
        else:
            assert division(num1, num2) == "Error: division by zero"

    print("All tests pass!")

# Run the automated test function
test_calculator()

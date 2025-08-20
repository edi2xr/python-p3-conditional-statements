# lib/control_flow.py

def admin_login(username, password):
    # Check if username is "admin" (any case) and password is correct
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    # Compare temperature ranges
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    # Multiples of both 3 and 5 come first
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    # Dictionary mapping operations to functions
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "ZeroDivisionError"
    }

    result = operations.get(operation, "Invalid operation!")
    
    if result == "ZeroDivisionError":
        print("Error: Cannot divide by zero")
        return None
    elif result == "Invalid operation!":
        print(result)
        return None
    else:
        return result

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


try:
    number = int(input("Enter a number to calculate its factorial: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = calculate_factorial(number)
        print(f"The factorial of {number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
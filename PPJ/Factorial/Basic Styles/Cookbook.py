# Global variable to hold the factorial result
factorial_result = 1

# Procedure to calculate the factorial of a number
def calculate_factorial(n):
    global factorial_result
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i

# Procedure to get input from the user
def get_input():
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        return number
    except ValueError:
        print("Please enter a valid integer.")
        return None

# Procedure to display the factorial result
def display_result():
    global factorial_result
    print(f"The factorial is: {factorial_result}")

# Main procedure to orchestrate the flow
number = get_input()
if number is not None and number >= 0:
    calculate_factorial(number)
    display_result()
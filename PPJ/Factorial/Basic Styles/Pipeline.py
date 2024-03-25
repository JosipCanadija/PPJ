# Function to calculate the factorial of a number
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Function to get input from the user
def get_input():
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        return number
    except ValueError:
        print("Please enter a valid integer.")
        return None

# Function to display the result
def display_result(result):
    print(f"The factorial is: {result}")

# Main function to orchestrate the flow
def main():
    number = get_input()
    if number is not None and number >= 0:
        result = calculate_factorial(number)
        display_result(result)

if __name__ == "__main__":
    main()

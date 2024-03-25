def create_factorial_calculator():
    calculator = {}

    def get_input():
        try:
            calculator['number'] = int(input("Enter a number to calculate its factorial: "))
        except ValueError:
            print("Please enter a valid integer.")

    def calculate_factorial():
        number = calculator.get('number')
        if number is None:
            print("Number not provided.")
            return
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        calculator['result'] = factorial

    def display_result():
        result = calculator.get('result')
        if result is not None:
            print(f"The factorial of {calculator['number']} is: {result}")
        else:
            print("Result not available.")

    calculator['get_input'] = get_input
    calculator['calculate_factorial'] = calculate_factorial
    calculator['display_result'] = display_result

    return calculator

def main():
    calculator = create_factorial_calculator()
    calculator['get_input']()
    calculator['calculate_factorial']()
    calculator['display_result']()

if __name__ == "__main__":
    main()

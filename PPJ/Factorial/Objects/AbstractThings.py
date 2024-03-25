class FactorialCalculatorAbstract:
    def get_input(self):
        raise NotImplementedError("Subclasses must implement get_input method.")

    def calculate_factorial(self):
        raise NotImplementedError("Subclasses must implement calculate_factorial method.")

    def display_result(self):
        raise NotImplementedError("Subclasses must implement display_result method.")

class FactorialCalculator(FactorialCalculatorAbstract):
    def __init__(self):
        self.number = None
        self.result = None

    def get_input(self):
        try:
            self.number = int(input("Enter a number to calculate its factorial: "))
        except ValueError:
            print("Please enter a valid integer.")

    def calculate_factorial(self):
        if self.number is None:
            print("Number not provided.")
            return
        factorial = 1
        for i in range(1, self.number + 1):
            factorial *= i
        self.result = factorial

    def display_result(self):
        if self.result is not None:
            print(f"The factorial of {self.number} is: {self.result}")
        else:
            print("Result not available.")

def main():
    calculator = FactorialCalculator()
    calculator.get_input()
    calculator.calculate_factorial()
    calculator.display_result()

if __name__ == "__main__":
    main()

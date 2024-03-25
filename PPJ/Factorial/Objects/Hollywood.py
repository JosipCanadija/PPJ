class FactorialCalculator:
    def __init__(self):
        self.number = None
        self.result = None
        self.callbacks = []

    def register_callback(self, callback):
        self.callbacks.append(callback)

    def notify_callbacks(self):
        for callback in self.callbacks:
            callback()

    def get_input(self):
        try:
            self.number = int(input("Enter a number to calculate its factorial: "))
        except ValueError:
            print("Please enter a valid integer.")
        self.notify_callbacks()

    def calculate_factorial(self):
        if self.number is None:
            print("Number not provided.")
            return
        factorial = 1
        for i in range(1, self.number + 1):
            factorial *= i
        self.result = factorial
        self.notify_callbacks()

    def display_result(self):
        if self.result is not None:
            print(f"The factorial of {self.number} is: {self.result}")
        else:
            print("Result not available.")
        self.notify_callbacks()

def main():
    calculator = FactorialCalculator()

    def calculate_and_display():
        calculator.calculate_factorial()
        calculator.display_result()

    calculator.register_callback(calculate_and_display)
    calculator.get_input()

if __name__ == "__main__":
    main()

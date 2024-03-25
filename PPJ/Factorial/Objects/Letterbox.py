class FactorialCalculator:
    def __init__(self):
        self.number = None
        self.result = None

    def receive_message(self, message):
        if message['type'] == 'input':
            self.number = message['data']
        elif message['type'] == 'calculate':
            self.calculate_factorial()
        elif message['type'] == 'display':
            self.display_result()
        else:
            print("Unknown message type.")

    def calculate_factorial(self):
        if self.number is None:
            print("Number not provided.")
            return
        factorial = 1
        for i in range(1, self.number + 1):
            factorial *= i
        self.result = factorial

    def display_result(self):
        if hasattr(self, 'result'):
            print(f"The factorial of {self.number} is: {self.result}")
        else:
            print("Result not available.")

def main():
    calculator = FactorialCalculator()
    calculator.receive_message({'type': 'input', 'data': int(input("Enter a number to calculate its factorial: "))})
    calculator.receive_message({'type': 'calculate'})
    calculator.receive_message({'type': 'display'})

if __name__ == "__main__":
    main()

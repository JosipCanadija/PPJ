class BulletinBoard:
    def __init__(self):
        self.subscriptions = {}
        self.events = []

    def subscribe(self, event_type, subscriber):
        if event_type not in self.subscriptions:
            self.subscriptions[event_type] = []
        self.subscriptions[event_type].append(subscriber)

    def publish(self, event):
        self.events.append(event)
        event_type = event['type']
        if event_type in self.subscriptions:
            for subscriber in self.subscriptions[event_type]:
                subscriber(event)

class FactorialCalculator:
    def __init__(self, bulletin_board):
        self.number = None
        self.result = None
        self.bulletin_board = bulletin_board

    def get_input(self, event):
        try:
            self.number = event['data']
        except ValueError:
            print("Please enter a valid integer.")

    def calculate_factorial(self, event):
        if self.number is None:
            print("Number not provided.")
            return
        factorial = 1
        for i in range(1, self.number + 1):
            factorial *= i
        self.result = factorial

    def display_result(self, event):
        if self.result is not None:
            print(f"The factorial of {self.number} is: {self.result}")
        else:
            print("Result not available.")

def main():
    bulletin_board = BulletinBoard()
    calculator = FactorialCalculator(bulletin_board)

    bulletin_board.subscribe('input', calculator.get_input)
    bulletin_board.subscribe('calculate', calculator.calculate_factorial)
    bulletin_board.subscribe('display', calculator.display_result)

    bulletin_board.publish({'type': 'input', 'data': int(input("Enter a number to calculate its factorial: "))})
    bulletin_board.publish({'type': 'calculate'})
    bulletin_board.publish({'type': 'display'})

if __name__ == "__main__":
    main()

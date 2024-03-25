def get_input(cont):
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        cont(number)
    except ValueError:
        print("Please enter a valid integer.")

def calculate_factorial(number, cont):
    def inner_factorial(n, acc):
        if n == 0:
            cont(acc)
        else:
            inner_factorial(n - 1, acc * n)
    inner_factorial(number, 1)

def display_result(result):
    print(f"The factorial is: {result}")

def main():
    get_input(lambda n: calculate_factorial(n, display_result))

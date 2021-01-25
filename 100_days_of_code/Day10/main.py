from art import logo

# Calculator

# Add


def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        opertaion_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[opertaion_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {opertaion_symbol} {num2} = {answer}")

        will_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if will_continue == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

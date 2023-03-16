from logo import logo
import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    continuation = True

    # Get the first number from the user
    number_1 = float(input("Enter your first number: "))

    # While the continuation flag is True
    while continuation:
        # Create a list of the available operations
        stored_operations = []
        for sign in operations.keys():
            stored_operations += sign
        # Print the available operations
        print(f"\n{stored_operations}")

        # Get the operation from the user
        operation_sign = input("Please select an operation symbol: ")

        # Get the next number from the user
        number_2 = float(input("\nEnter your next number: "))

        # Get the function corresponding to the selected operation sign
        operation_formula = operations[operation_sign]

        # Calculate the result using the selected operation
        result = operation_formula(number_1, number_2)

        # Print the calculation result
        print(f"\n{number_1} {operation_sign} {number_2} = {result}")

        # Ask the user if they want to continue using the result as the first number
        if input(f"\nDo you want to continue to calculate the {result}, again? Type 'Y' or 'N' \n").lower() == "y":
            number_1 = result
        else:
            # If the user does not want to continue, set the continuation flag to False
            # Clear the screen and call the calculator function again
            continuation = False
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()


calculator()



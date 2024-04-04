from typing import Union
from math import inf

LOGO = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


########################################################################################################################

def _collect_number(message: str) -> float:
    """
    Print the message from the param and collect a float or integer from the user.
    :param message: input prompt
    :return: float or integer provided by the user
    """

    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid value. Integer or float required. Try again.")


########################################################################################################################

def _collect_operator() -> str:
    """
    Collect an operator from the user. Possible operators are +, -, *, /.
    :return: one of the operators +, -, *, /
    """

    while True:
        operator = input("Pick an operation [+-*/]: ")
        if operator in ("+", "-", "*", "/"):
            return operator
        else:
            print("Invalid value. One of the operators +, -, *, / required. Try again.")


########################################################################################################################

def _run_calculation(num1: float, num2: float, operator: str) -> Union[float, None]:
    """
    :param num1: operand 1
    :param num2: operand 2
    :param operator: operator
    :return: result of operand 1 operator operand 2
    """

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return inf
    else:
        # shouldn't happen
        return None


########################################################################################################################

def run_program() -> None:
    """
    Run the calculator. Let the user input either both numbers of the operation or leave the first one as the result of
    the previous operation.
    """

    print(LOGO)
    num1 = None

    while True:
        if num1 is None:
            num1 = _collect_number("What's the first number?: ")
        else:
            print(f"First number is {num1}.")
        operator = _collect_operator()
        num2 = _collect_number("What's the next number?: ")
        result = _run_calculation(num1, num2, operator)
        if result is not None:
            print(f"{num1} {operator} {num2} = {result}")
        else:
            print("Something went wrong with the calculation.")

        while True:
            print("Press Ctrl+C to exit, or:")
            if result is not None and result is not inf:
                print(f"-type \"(y)es\" to continue calculating with {result}")
                print("-type \"(n)o\" to start a new calculation")
                continue_calculation = input("> ").strip().lower()

                if continue_calculation in ("y", "yes"):
                    num1 = result
                    break
                elif continue_calculation in ("n", "no"):
                    num1 = None
                    break
                else:
                    print("Invalid value. (Y)es or (N)o required. Try again.")
            else:
                num1 = None
                print("Press Enter to start a new calculation.")
                input()
                break

########################################################################################################################

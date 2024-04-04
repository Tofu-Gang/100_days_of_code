from typing import Union

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

    :param message:
    :return:
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

    :return:
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

    :param num1:
    :param num2:
    :param operator:
    :return:
    """

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return None


########################################################################################################################

def run_program() -> None:
    """

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
        print(f"{num1} {operator} {num2} = {result}")

        while True:
            print("Press Ctrl+C to exit, or:")
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


########################################################################################################################

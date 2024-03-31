########################################################################################################################

def calculate_tip(total_bill: float, tip: int, people_count: int) -> float:
    """
    :param total_bill: total bill amount
    :param tip: tip amount (in percentage)
    :param people_count: how many people split the bill
    :return: how much should each person pay, splitting the bill evenly, including the selected tip
    """

    return (total_bill + (total_bill / 100 * tip)) / people_count


########################################################################################################################

def run_program() -> None:
    """
    Collect both demanded user inputs and generate a possible band name from those inputs.
    """

    print("Welcome to the tip calculator!")

    total_bill = None
    while True:
        try:
            total_bill = float(input("What was the total bill? $"))
            break
        except ValueError:
            print("Invalid value. Integer or a real number with decimal point required.")
            continue

    tip = None
    while True:
        try:
            tip = int(input("How much tip would you like to give? 10, 12, or 15? > "))
            if tip not in (10, 12, 15):
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid value. Integer 10, 12 or 15 required.")
            continue

    people_count = None
    while True:
        try:
            people_count = int(input("How many people to split the bill? > "))
            break
        except ValueError:
            print("Invalid value. Integer required.")
            continue

    print("Each person should pay: ${:.2f}".format(calculate_tip(total_bill, tip, people_count)))


########################################################################################################################

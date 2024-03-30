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
    total_bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? >"))
    people_count = int(input("How many people to split the bill? >"))
    print("Each person should pay: ${:.2f}".format(calculate_tip(total_bill, tip, people_count)))


########################################################################################################################

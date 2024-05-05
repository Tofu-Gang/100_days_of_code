from smtplib import SMTP
from os.path import join, dirname, realpath
from datetime import datetime
from typing import Union
from random import choice


########################################################################################################################

QUOTES_FILE_PATH = join(dirname(realpath(__file__)), "quotes.txt")
PASSWORD_FILE_PATH = join(dirname(realpath(__file__)), "pass.txt")
# TODO: fill in the email that matches the password that returns the _read_password() function
EMAIL = None


########################################################################################################################

def _read_password() -> Union[str, None]:
    """
    :return: email password
    """

    try:
        with open(join(dirname(realpath(__file__)), "pass.txt"), "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


########################################################################################################################

def _send_email(subject: str, message: str, recipients: str) -> None:
    """
    Send an email. Get subject, message and recipients from the params.
    :param subject: email subject
    :param message: email message
    :param recipients: recipient(s) of the email
    """

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=_read_password())
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=recipients,
                            msg=f"Subject:{subject}\n\n{message}")


########################################################################################################################

def _get_random_quote() -> str:
    """
    :return: random quote from the quotes file
    """

    with open(QUOTES_FILE_PATH, "r") as f:
        return choice(f.readlines()).strip()


########################################################################################################################

def run_program() -> None:
    """

    """

    if datetime.now().weekday() == 0:
        _send_email("Monday Motivation", _get_random_quote(), None)


########################################################################################################################

from smtplib import SMTP
from os.path import join, dirname, realpath
from datetime import datetime
from pandas import read_csv
from random import choice

from .birthday_person import BirthdayPerson


########################################################################################################################

class AutomatedBirthdayWisher:
    _PASSWORD_FILE_PATH = join(dirname(realpath(__file__)), "pass.txt")
    _BIRTHDAYS_FILE_PATH = join(dirname(realpath(__file__)), "birthdays.csv")
    _LETTER_1_FILE_PATH = join(dirname(realpath(__file__)), "letter_templates", "letter_1.txt")
    _LETTER_2_FILE_PATH = join(dirname(realpath(__file__)), "letter_templates", "letter_2.txt")
    _LETTER_3_FILE_PATH = join(dirname(realpath(__file__)), "letter_templates", "letter_3.txt")

########################################################################################################################

    def __init__(self):
        """

        """

        self._email = ""
        self._load_password()
        self._load_birthdays()
        self._load_letters()
        self._today = datetime.now()

########################################################################################################################

    def _load_password(self) -> None:
        """
        Read password to the email that is used for sending. This file exists only locally, for security reasons. No
        email or password will be under VCS.
        """

        try:
            with open(join(dirname(realpath(__file__)), "pass.txt"), "r") as f:
                self._password = f.read().strip()
        except FileNotFoundError:
            self._password = None

########################################################################################################################

    def _load_birthdays(self) -> None:
        """
        Read the csv file with birthday people data and store them as instances of BirthdayPerson class.
        """

        frame = read_csv(self._BIRTHDAYS_FILE_PATH)
        name_key = frame.columns[0]
        email_key = frame.columns[1]
        year_key = frame.columns[2]
        month_key = frame.columns[3]
        day_key = frame.columns[4]

        self._birthday_people = tuple(BirthdayPerson(name=row[name_key].strip(),
                                                     email=row[email_key].strip(),
                                                     year=int(row[year_key]),
                                                     month=int(row[month_key]),
                                                     day=int(row[day_key]))
                                      for row in frame.to_dict(orient="records"))

########################################################################################################################

    def _load_letters(self) -> None:
        """
        Load birthday wishes templates and store them as a Tuple.
        """

        self._letters = []
        with open(self._LETTER_1_FILE_PATH, "r") as f:
            self._letters.append(f.read().strip())
        with open(self._LETTER_2_FILE_PATH, "r") as f:
            self._letters.append(f.read().strip())
        with open(self._LETTER_3_FILE_PATH, "r") as f:
            self._letters.append(f.read().strip())
        self._letters = tuple(self._letters)

########################################################################################################################

    def _personalize_random_letter(self, name: str) -> str:
        """
        :param name: birthday person name
        :return: random personalized birthday wish as a string
        """

        return choice(self._letters).replace("[NAME]", name)

########################################################################################################################

    def _send_email(self, subject: str, message: str, recipients: str) -> None:
        """
        Send an email. Get subject, message and recipients from the params.

        :param subject: email subject
        :param message: email message
        :param recipients: recipient(s) of the email
        """

        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self._email, password=self._password)
            connection.sendmail(from_addr=self._email,
                                to_addrs=recipients,
                                msg=f"Subject:{subject}\n\n{message}")


########################################################################################################################

def run_program() -> None:
    """

    """

    # 1. Update the birthdays.csv
    # 2. Check if today matches a birthday in the birthdays.csv
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # 4. Send the letter generated in step 3 to that person's email address.
    AutomatedBirthdayWisher()

########################################################################################################################

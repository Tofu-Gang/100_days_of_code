########################################################################################################################

class BirthdayPerson:

    def __init__(self, name: str, email: str, year: int, month: int, day: int):
        """
        Create a birthday person. They have a name and email. Their birthday is separated into year, month and day.

        :param name: birthday person name
        :param email: birthday person email
        :param year: birthday year
        :param month: birthday month
        :param day: birthday day
        """

        self._name = name
        self._email = email
        self._year = year
        self._month = month
        self._day = day

########################################################################################################################

    @property
    def name(self) -> str:
        """
        :return: name of the birthday person
        """

        return self._name

########################################################################################################################

    @property
    def email(self) -> str:
        """
        :return: email of the birthday person
        """

        return self._email

########################################################################################################################

    @property
    def year(self) -> int:
        """
        :return: birthday year
        """

        return self._year

########################################################################################################################

    @property
    def month(self) -> int:
        """
        :return: birthday month
        """

        return self._month

########################################################################################################################

    @property
    def day(self) -> int:
        """
        :return: birthday day
        """

        return self._day


########################################################################################################################

class Question:

    def __init__(self, text: str, answer: bool):
        """
        A question has a text and an answer.

        :param text: question text
        :param answer: question answer
        """

        self._text = text
        self._answer = answer

########################################################################################################################

    @property
    def text(self) -> str:
        """
        :return: question text
        """

        return self._text

########################################################################################################################

    @property
    def answer(self) -> bool:
        """
        :return: question answer
        """

        return self._answer

########################################################################################################################

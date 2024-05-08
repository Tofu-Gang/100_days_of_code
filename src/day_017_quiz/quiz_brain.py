from random import choice
from requests import get
from json import loads
from html import unescape

from .question_model import Question


########################################################################################################################

class QuizzBrain:

    def __init__(self):
        """
        Set the questions and score counters to zero. Load question bank. Create temporary variable where the current
        question will be stored between function calls.
        """

        self._question = None
        self._question_number = 0
        self._score = 0
        response = get("https://opentdb.com/api.php", params={
            "amount": 10,
            "type": "boolean"
        })
        response.raise_for_status()

        self._question_bank = list(Question(unescape(question["question"]), eval(question["correct_answer"]))
                                   for question in response.json()["results"])

########################################################################################################################

    @property
    def score(self) -> int:
        """
        :return: the user score
        """

        return self._score

########################################################################################################################

    @property
    def questions_passed(self) -> int:
        """
        :return: how many questions was the user asked so far
        """

        return self._question_number

########################################################################################################################

    @property
    def current_question(self) -> Question:
        """
        :return: current question object
        """

        return self._question

########################################################################################################################

    @property
    def still_has_questions(self) -> bool:
        """
        :return: True if there are questions left, False otherwise
        """

        return len(self._question_bank) > 0

########################################################################################################################

    def check_answer(self, answer: bool) -> bool:
        """
        :param answer: user answer
        :return: True if the user answer was correct, False otherwise
        """

        if self._question.answer == answer:
            self._score += 1
            return True
        else:
            return False

########################################################################################################################

    def next_question(self) -> None:
        """
        Move on to the next question.
        """

        self._question_number += 1
        self._question = choice(self._question_bank)
        self._question_bank.remove(self._question)

########################################################################################################################

from random import choice

from .data import question_data, TEXT_KEY, ANSWER_KEY
from .question_model import Question


########################################################################################################################

class QuizzBrain:

    def __init__(self):
        """
        Set the questions counter for display purposes. Set the user score to zero. Load question bank. Create temporary
        variables where the current question and user answer will be stored between function calls.
        """

        self._question_number = 0
        self._question_bank = list(Question(question[TEXT_KEY], eval(question[ANSWER_KEY]))
                                   for question in question_data)
        self._score = 0
        self._question = None
        self._answer = None

########################################################################################################################

    def still_has_questions(self) -> bool:
        """
        :return: True if there are questions left, False otherwise
        """

        return len(self._question_bank) > 0

########################################################################################################################

    def check_answer(self) -> None:
        """
        Checks the user answer and displays the result.
        """

        if self._question.answer == self._answer:
            print("You got it right!")
            self._score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self._question.answer}.")
        print(f"Your current score is: {self._score}/{self._question_number}")

        self._question = None
        self._answer = None

########################################################################################################################

    def next_question(self) -> None:
        """
        Display the question. Get the answer from the user.
        """

        self._question_number += 1
        self._question = choice(self._question_bank)

        while True:
            answer = input(f"Q.{self._question_number}: {self._question.text} (True/False)?: ").strip().upper()

            if answer in ("T", "TRUE"):
                self._answer = True
                break
            elif answer in ("F", "FALSE"):
                self._answer = False
                break
            else:
                print("Invalid value. Please try again.")

        self._question_bank.remove(self._question)

########################################################################################################################

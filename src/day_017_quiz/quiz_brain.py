from random import choice

from .data import question_data, TEXT_KEY, ANSWER_KEY
from .question_model import Question


########################################################################################################################

class QuizzBrain:

    def __init__(self):
        """
        Set the questions counter for display purposes. Load question bank.
        """

        self._question_number = 1
        self._question_bank = list(Question(question[TEXT_KEY], bool(question[ANSWER_KEY]))
                                   for question in question_data)

########################################################################################################################

    def next_question(self) -> bool | None:
        """
        Display the question. Get the answer from the user.

        :return: True for correct answer, False for incorrect, None if no question can be displayed.
        """

        try:
            question = choice(self._question_bank)

            while True:
                answer = input(f"Q.{self._question_number}: {question.text} (True/False)?: ").strip().upper()

                if answer in ("T", "TRUE"):
                    answer = True
                    break
                elif answer in ("F", "FALSE"):
                    answer = False
                    break
                else:
                    print("Invalid value. Please try again.")

            self._question_bank.remove(question)
            self._question_number += 1
            return bool(answer) == question.answer
        except IndexError:
            print("No more questions. You win the game!")
            return None

########################################################################################################################

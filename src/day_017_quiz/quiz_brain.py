from .data import question_data, TEXT_KEY, ANSWER_KEY
from .question_model import Question


########################################################################################################################

class QuizzBrain:

    def __init__(self):
        """
        Set the questions counter for display purposes. Load question bank.
        """

        self._question_number = 0
        self._question_bank = list(Question(question[TEXT_KEY], bool(question[ANSWER_KEY]))
                                   for question in question_data)

########################################################################################################################

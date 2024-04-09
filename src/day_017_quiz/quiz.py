from .data import question_data, TEXT_KEY, ANSWER_KEY
from .question_model import Question


########################################################################################################################

def run_program() -> None:
    """

    """

    question_bank = list(Question(question[TEXT_KEY], bool(question[ANSWER_KEY]))
                         for question in question_data)


########################################################################################################################

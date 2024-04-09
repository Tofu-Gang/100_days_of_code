from .quiz_brain import QuizzBrain


########################################################################################################################

def run_program() -> None:
    """

    """

    quizz_brain = QuizzBrain()

    while quizz_brain.still_has_questions():
        quizz_brain.next_question()
        quizz_brain.check_answer()

########################################################################################################################

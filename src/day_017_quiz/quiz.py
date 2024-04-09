from .quiz_brain import QuizzBrain


########################################################################################################################

def run_program() -> None:
    """

    """

    quizz_brain = QuizzBrain()

    while quizz_brain.still_has_questions():
        quizz_brain.next_question()
        quizz_brain.check_answer()
        print("\n")
    print("You've completed the quiz.")
    print(f"Your final score was: {quizz_brain.score}/{quizz_brain.questions_passed}")

########################################################################################################################

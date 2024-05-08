from .quiz_brain import QuizzBrain
from .question_model import Question


########################################################################################################################

def _get_user_answer(question: Question, question_number: int) -> bool:
    """
    :param question: current question
    :param question_number: current question number
    :return: True or False, based on user choice
    """

    while True:
        answer = input(f"Q.{question_number}: {question.text} (True/False)?: ").strip().upper()

        if answer in ("T", "TRUE"):
            return True
        elif answer in ("F", "FALSE"):
            return False
        else:
            print("Invalid value. Please try again.")


########################################################################################################################

def run_program() -> None:
    """
    Go through the quizz with random T/F questions.
    """

    quizz_brain = QuizzBrain()

    while quizz_brain.still_has_questions:
        quizz_brain.next_question()
        question = quizz_brain.current_question
        answer = _get_user_answer(question, quizz_brain.questions_passed)
        correct = quizz_brain.check_answer(answer)

        if correct:
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question.answer}.")
        if quizz_brain.still_has_questions:
            print(f"Your current score is: {quizz_brain.score}/{quizz_brain.questions_passed}")

    print("You've completed the quiz.")
    print(f"Your final score was: {quizz_brain.score}/{quizz_brain.questions_passed}")

########################################################################################################################

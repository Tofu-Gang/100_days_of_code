from tkinter import Tk, Canvas, PhotoImage, Button, Label
from os.path import join, dirname, realpath

from src.day_017_quiz.quiz_brain import QuizzBrain


########################################################################################################################

class QuizGUI:
    _THEME_COLOR = "#375362"
    _TRUE_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), "img", "true.png")
    _FALSE_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), "img", "false.png")

########################################################################################################################

    def __init__(self):
        """
        Set up the window and controls. Create the question database. Show the first question.
        """

        self._set_display()
        self._set_controls()
        self._quiz_brain = QuizzBrain()
        self._next_question()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """
        Create the window, main area for displaying questions and score label. Set up geometry and colors.
        """

        self._window = Tk()
        self._window.title("Quizzler")
        self._window.config(padx=20, pady=20, bg=self._THEME_COLOR)

        self._score_label = Label(bg=self._THEME_COLOR, fg="white")
        self._score_label.grid(row=0, column=1)

        self._canvas = Canvas(width=300, height=250)
        self._question_text = self._canvas.create_text(
            150, 125, width=280, fill=self._THEME_COLOR, font=("Arial", 20, "italic"))
        self._canvas.grid(row=1, column=0, columnspan=2, pady=50)

########################################################################################################################

    def _set_controls(self) -> None:
        """
        Create two buttons, one for answer "TRUE" and one for answer "FALSE".
        """

        self._true_image = PhotoImage(file=self._TRUE_IMAGE_FILE_PATH)
        self._false_image = PhotoImage(file=self._FALSE_IMAGE_FILE_PATH)
        self._true_button = Button(image=self._true_image,
                                   highlightthickness=0,
                                   command=lambda: self._check_answer(True))
        self._true_button.grid(row=2, column=0)
        self._false_button = Button(image=self._false_image,
                                    highlightthickness=0,
                                    command=lambda: self._check_answer(False))
        self._false_button.grid(row=2, column=1)

########################################################################################################################

    def _check_answer(self, answer: bool) -> None:
        """
        Pass the user answer to the quizz brain to evaluate it. Make visual feedback so the user knows they were correct
        or wrong. Move on to the next question or show the final message if there are no more questions available.

        :param answer: user answer; True for correct, False for incorrect
        """

        correct = self._quiz_brain.check_answer(answer)
        self._score_label.configure(text=f"Score: {self._quiz_brain.score}", fg="white", bg=self._THEME_COLOR)
        self._true_button.configure(state="disabled")
        self._false_button.configure(state="disabled")

        if correct:
            self._canvas.configure(bg="green")
        else:
            self._canvas.configure(bg="red")

        if self._quiz_brain.still_has_questions:
            self._window.after(1000, self._next_question)
        else:
            self._window.after(1000, self._end_quiz)

########################################################################################################################

    def _next_question(self) -> None:
        """
        Move on to the next question.
        """

        self._quiz_brain.next_question()
        self._true_button.configure(state="normal")
        self._false_button.configure(state="normal")
        self._canvas.configure(bg="white")
        self._canvas.itemconfig(
            self._question_text,
            text=f"Q.{self._quiz_brain.questions_passed}: {self._quiz_brain.current_question.text}")

########################################################################################################################

    def _end_quiz(self) -> None:
        """
        Finish the quizz and display the final score.
        """

        self._canvas.configure(bg="white")
        self._score_label.configure(text=f"Score: {self._quiz_brain.score}", fg="white", bg=self._THEME_COLOR)
        self._canvas.itemconfig(
            self._question_text,
            text=f"Quizz Finished! Your final score is: {self._quiz_brain.score}/{self._quiz_brain.questions_passed}")


########################################################################################################################

def run_program() -> None:
    """
    Run the quizz application.
    """

    QuizGUI()


########################################################################################################################

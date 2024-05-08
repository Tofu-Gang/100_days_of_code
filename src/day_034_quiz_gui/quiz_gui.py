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

        """

        self._set_display()
        self._set_controls()
        self._quiz_brain = QuizzBrain()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """

        """

        self._window = Tk()
        self._window.title("Quizzler")
        self._window.config(padx=20, pady=20, bg=self._THEME_COLOR)

        self._score_label = Label(text="Score: 0", bg=self._THEME_COLOR, fg="white")
        self._score_label.grid(row=0, column=1)

        self._canvas = Canvas(width=300, height=250, bg="white")
        self._question_text = self._canvas.create_text(
            150, 125, text="Some question text", fill=self._THEME_COLOR, font=("Arial", 20, "italic"))
        self._canvas.grid(row=1, column=0, columnspan=2, pady=50)

########################################################################################################################

    def _set_controls(self) -> None:
        """

        """

        self._true_image = PhotoImage(file=self._TRUE_IMAGE_FILE_PATH)
        self._false_image = PhotoImage(file=self._FALSE_IMAGE_FILE_PATH)
        Button(image=self._true_image, highlightthickness=0, command=lambda: self._check_answer(True)).grid(row=2, column=0)
        Button(image=self._false_image, highlightthickness=0, command=lambda: self._check_answer(False)).grid(row=2, column=1)

########################################################################################################################

    def _check_answer(self, answer: bool) -> None:
        """

        :param answer:
        :return:
        """

        pass


########################################################################################################################

def run_program() -> None:
    """

    """

    QuizGUI()


########################################################################################################################

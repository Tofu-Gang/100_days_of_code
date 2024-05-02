from tkinter import Tk, PhotoImage, Canvas, Label, Button
from os.path import join, dirname, realpath


########################################################################################################################

class FlashCards:
    _BACKGROUND_COLOR = "#B1DDC6"
    _WINDOW_PADDING = 50
    _CARD_FRONT_IMG_PATH = join(dirname(realpath(__file__)), "images", "card_front.png")
    _CARD_BACK_IMG_PATH = join(dirname(realpath(__file__)), "images", "card_back.png")
    _RIGHT_IMG_PATH = join(dirname(realpath(__file__)), "images", "right.png")
    _WRONG_IMG_PATH = join(dirname(realpath(__file__)), "images", "wrong.png")

########################################################################################################################

    def __init__(self):
        """
        Create the window, set up all the widgets, geometry, images and colors. Show the window.
        """

        self._set_display()
        self._set_controls()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """
        Create the window with a flashcard picture and two labels: one for the display language and the other for a
        word in that language. Configure the geometry.
        """

        self._window = Tk()
        self._window.title("Flashy")
        self._window.configure(padx=self._WINDOW_PADDING, pady=self._WINDOW_PADDING, bg=self._BACKGROUND_COLOR)

        self._card_front_img = PhotoImage(file=self._CARD_FRONT_IMG_PATH)
        self._card_back_img = PhotoImage(file=self._CARD_BACK_IMG_PATH)
        width = self._card_front_img.width()
        height = self._card_front_img.height()

        self._canvas = Canvas(width=width, height=height, highlightthickness=0, bg=self._BACKGROUND_COLOR)
        self._canvas.create_image(width / 2, height / 2, image=self._card_front_img)
        self._canvas.grid(row=0, column=0, rowspan=2, columnspan=2)

        self._lang_label = Label(text="French", bg="#FFFFFF", font=("Arial", 40, "italic"))
        self._lang_label.grid(row=0, column=0, columnspan=2)

        self._word_label = Label(text="trouve", bg="#FFFFFF", font=("Arial", 60, "bold"))
        self._word_label.grid(row=1, column=0, columnspan=2, sticky="N")

########################################################################################################################

    def _set_controls(self) -> None:
        """
        Create two buttons. One "right", which the user presses if they know the displayed word. The other, "wrong",
        which the user presses if they do not know the displayed word. Connect those two buttons with their respective
        methods.
        """

        self._right_img = PhotoImage(file=self._RIGHT_IMG_PATH)
        self._wrong_img = PhotoImage(file=self._WRONG_IMG_PATH)
        Button(image=self._right_img, highlightthickness=0, command=self._right).grid(row=2, column=0)
        Button(image=self._wrong_img, highlightthickness=0, command=self._wrong).grid(row=2, column=1)

########################################################################################################################

    def _right(self) -> None:
        """
        
        """

        print("right")

########################################################################################################################

    def _wrong(self) -> None:
        """

        """

        print("wrong")


########################################################################################################################

def run_program() -> None:
    """

    """

    FlashCards()


########################################################################################################################

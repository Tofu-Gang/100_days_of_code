from tkinter import Tk, PhotoImage, Canvas, Label, Button
from os.path import join, dirname, realpath

from .words_engine import WordsEngine


########################################################################################################################

class FlashCards:
    _WINDOW_BG_COLOR = "#B1DDC6"
    _WINDOW_PADDING = 50
    _CARD_FRONT_IMG_PATH = join(dirname(realpath(__file__)), "images", "card_front.png")
    _CARD_BACK_IMG_PATH = join(dirname(realpath(__file__)), "images", "card_back.png")
    _CARD_FRONT_BG_COLOR = "#FFFFFF"
    _CARD_BACK_BG_COLOR = "#91C2AF"
    _RIGHT_IMG_PATH = join(dirname(realpath(__file__)), "images", "right.png")
    _WRONG_IMG_PATH = join(dirname(realpath(__file__)), "images", "wrong.png")

########################################################################################################################

    def __init__(self):
        """
        Create the window, set up all the widgets, geometry, images and colors. Start the learning session and show the
        window.
        """

        self._set_display()
        self._set_controls()
        self._words_engine = WordsEngine()
        self._start_learning()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """
        Create the window with a flashcard picture and two labels: one for the display language and the other for a
        word in that language. Configure the geometry.
        """

        self._window = Tk()
        self._window.title("Flashy")
        self._window.configure(padx=self._WINDOW_PADDING, pady=self._WINDOW_PADDING, bg=self._WINDOW_BG_COLOR)
        self._window.protocol("WM_DELETE_WINDOW", self._on_closing)

        self._card_front_img = PhotoImage(file=self._CARD_FRONT_IMG_PATH)
        self._card_back_img = PhotoImage(file=self._CARD_BACK_IMG_PATH)

        self._canvas = Canvas(width=self._card_front_img.width(),
                              height=self._card_front_img.height(),
                              highlightthickness=0,
                              bg=self._WINDOW_BG_COLOR)
        self._canvas.grid(row=0, column=0, rowspan=2, columnspan=2)

        self._lang_label = Label(font=("Arial", 40, "italic"))
        self._lang_label.grid(row=0, column=0, columnspan=2)

        self._word_label = Label(font=("Arial", 60, "bold"))
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

    def _start_learning(self) -> None:
        """
        Start the learning session.
        """

        self._next_word()

########################################################################################################################

    def _next_word(self) -> None:
        """
        Choose another word. Show its original form. Set a timer for flipping the card and showing its translation.
        """

        self._word = self._words_engine.get_random_word()
        self._card_flipped = False
        self._show_word()
        self._window.after(3000, self._flip_card)

########################################################################################################################

    def _show_word(self) -> None:
        """
        Show the param word in the window.
        """

        if self._card_flipped:
            image = self._card_back_img
            lang = self._words_engine.translation_lang
            word = self._word.translation
            bg_color = self._CARD_BACK_BG_COLOR
        else:
            image = self._card_front_img
            lang = self._words_engine.original_lang
            word = self._word.original
            bg_color = self._CARD_FRONT_BG_COLOR

        self._canvas.create_image(image.width() / 2, image.height() / 2, image=image)
        self._lang_label.configure(text=lang, bg=bg_color)
        self._word_label.configure(text=word, bg=bg_color)

########################################################################################################################

    def _flip_card(self) -> None:
        """
        Flip the card and show the word translation.
        """

        self._card_flipped = True
        self._show_word()

########################################################################################################################

    def _right(self) -> None:
        """
        The user knows the current word, remove it from the database. Show another word.
        """

        self._words_engine.remove_word(self._word)
        self._next_word()

########################################################################################################################

    def _wrong(self) -> None:
        """
        The user did not know the current word, show another one.
        """

        self._next_word()

########################################################################################################################

    def _on_closing(self) -> None:
        """
        Save the words that the user still needs to learn to a file before closing the window.
        """

        self._words_engine.save_words()
        self._window.destroy()


########################################################################################################################

def run_program() -> None:
    """
    Run the Flash Cards program.
    """

    FlashCards()


########################################################################################################################

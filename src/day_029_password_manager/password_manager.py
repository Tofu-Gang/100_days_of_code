from tkinter import Tk, PhotoImage, Canvas
from os.path import join, dirname, realpath


########################################################################################################################

class PasswordManager:
    _BG_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), "logo.png")
    _WINDOW_PADDING = 20
    _LOGO_WIDTH = 200
    _LOGO_HEIGHT = 200

########################################################################################################################

    def __init__(self):
        """

        """

        self._set_display()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """

        """

        self._window = Tk()
        self._window.title("Password Manager")
        self._window.configure(padx=self._WINDOW_PADDING, pady=self._WINDOW_PADDING)

        # could be set as a local variable, but I guess the garbage collector deletes it and then the image won't get
        # displayed at all
        self._logo_img = PhotoImage(file=self._BG_IMAGE_FILE_PATH)
        self._canvas = Canvas(width=self._LOGO_WIDTH, height=self._LOGO_HEIGHT, highlightthickness=0)
        self._canvas.create_image(self._LOGO_WIDTH / 2, self._LOGO_HEIGHT / 2, image=self._logo_img)
        self._canvas.pack()


########################################################################################################################

def run_program() -> None:
    """

    """

    PasswordManager()


########################################################################################################################

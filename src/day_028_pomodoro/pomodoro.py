from tkinter import Tk, Canvas, PhotoImage
from os.path import join, dirname, realpath


########################################################################################################################
class Pomodoro:
    BG_IMAGE_FILE_NAME = "tomato.png"
    BG_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), BG_IMAGE_FILE_NAME)
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT = ("Courier", 27, "bold")
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20
    WINDOW_PAD_X = 100
    WINDOW_PAD_Y = 50

########################################################################################################################

    def __init__(self):
        """
        Create the main window, set up background picture and the main counter.
        """

        self._window = Tk()
        self._set_window()
        self._canvas = Canvas()
        # could be set as a local variable, but I guess the garbage collector deletes it and then the image won't get
        # displayed at all
        self._tomato_img = PhotoImage(file=self.BG_IMAGE_FILE_PATH)
        self._set_canvas()
        self._window.mainloop()

########################################################################################################################

    def _set_window(self) -> None:
        """
        Set the title, background color and geometry of the main window.
        """

        self._window.title("Pomodoro")
        self._window.configure(padx=self.WINDOW_PAD_X, pady=self.WINDOW_PAD_Y, bg=self.YELLOW)

########################################################################################################################

    def _set_canvas(self) -> None:
        """
        Set the background color and picture and its geometry. Set up the main clock counter.
        """

        tomato_width = self._tomato_img.width()
        tomato_height = self._tomato_img.height()
        tomato_pos_x = tomato_width / 2
        # the image is cut on the bottom for some reason, subtract some pixels from the y positions to fix that
        tomato_pos_y = tomato_height / 2 - 1
        counter_label_pos_x = tomato_pos_x
        counter_label_pos_y = tomato_pos_y + 18

        self._canvas.configure(width=tomato_width, height=tomato_height, bg=self.YELLOW, highlightthickness=False)
        self._canvas.create_image(tomato_pos_x, tomato_pos_y, image=self._tomato_img)
        self._canvas.create_text(counter_label_pos_x, counter_label_pos_y, text="00:00", fill="white", font=self.FONT)
        self._canvas.pack()


########################################################################################################################

def run_program() -> None:
    """
    Run the Pomodoro application.
    """

    Pomodoro()


########################################################################################################################

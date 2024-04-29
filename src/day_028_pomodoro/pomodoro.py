from tkinter import Tk, Canvas, PhotoImage, Label, Button
from os.path import join, dirname, realpath
from datetime import datetime, timedelta


########################################################################################################################

class Pomodoro:
    BG_IMAGE_FILE_NAME = "tomato.png"
    BG_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), BG_IMAGE_FILE_NAME)
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    COUNTER_FONT = ("Courier", 27, "bold")
    INFO_FONT = ("Courier", 40, "bold")
    WINDOW_PAD_X = 100
    WINDOW_PAD_Y = 50
    WORK_PHASE_LABEL = "Work"
    BREAK_PHASE_LABEL = "Break"
    LABEL_KEY = "LABEL"
    TIME_KEY = "TIME"
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20

    WORK_PHASE = {
        LABEL_KEY: WORK_PHASE_LABEL,
        TIME_KEY: WORK_MIN
    }
    SHORT_BREAK_PHASE = {
        LABEL_KEY: BREAK_PHASE_LABEL,
        TIME_KEY: SHORT_BREAK_MIN
    }
    LONG_BREAK_PHASE = {
        LABEL_KEY: BREAK_PHASE_LABEL,
        TIME_KEY: LONG_BREAK_MIN
    }
    PHASES = (WORK_PHASE,
              SHORT_BREAK_PHASE,
              WORK_PHASE,
              SHORT_BREAK_PHASE,
              WORK_PHASE,
              SHORT_BREAK_PHASE,
              WORK_PHASE,
              LONG_BREAK_PHASE)

########################################################################################################################

    def __init__(self):
        """
        Set up the display widgets and window controls. Finally, show the main window.
        """

        self._set_display()
        self._set_controls()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """
        Create the main window with a background image. Set up the colors and geometry. Create the main info label above
        the tomato picture and progress label (checkmarks) between the buttons.
        """

        self._window = Tk()
        self._window.title("Pomodoro")
        self._window.configure(padx=self.WINDOW_PAD_X, pady=self.WINDOW_PAD_Y, bg=self.YELLOW)

        # could be set as a local variable, but I guess the garbage collector deletes it and then the image won't get
        # displayed at all
        self._tomato_img = PhotoImage(file=self.BG_IMAGE_FILE_PATH)
        tomato_width = self._tomato_img.width()
        tomato_height = self._tomato_img.height()
        tomato_pos_x = tomato_width / 2
        # the image is cut on the bottom for some reason, subtract some pixels from the y positions to fix that
        tomato_pos_y = tomato_height / 2 - 1
        counter_label_pos_x = tomato_pos_x
        counter_label_pos_y = tomato_pos_y + 18

        self._canvas = Canvas(width=tomato_width, height=tomato_height, bg=self.YELLOW, highlightthickness=0)
        self._canvas.create_image(tomato_pos_x, tomato_pos_y, image=self._tomato_img)
        self._counter_label = self._canvas.create_text(counter_label_pos_x, counter_label_pos_y,
                                                       fill="white", font=self.COUNTER_FONT)
        self._canvas.grid(row=1, column=1)

        self._info_label = Label(text="Pomodoro", fg=self.GREEN, bg=self.YELLOW, font=self.INFO_FONT)
        self._info_label.grid(row=0, column=1)
        self._progress_label = Label(fg=self.GREEN, bg=self.YELLOW)
        self._progress_label.grid(row=3, column=1)

########################################################################################################################

    def _set_controls(self) -> None:
        """
        Create the start and reset buttons, connect them to their respective methods and place them in the main window.
        """

        self._start_button = Button(text="Start", command=self._start, highlightthickness=0)
        self._start_button.grid(row=2, column=0)
        self._reset_button = Button(text="Reset", command=self._reset, highlightthickness=0)
        self._reset_button.grid(row=2, column=2)

########################################################################################################################

    def _start(self) -> None:
        """
        Go to the first phase of the pomodoro routine. Start the timer.
        """

        self._phase = 0
        self._update_info()
        self._set_counter()

########################################################################################################################

    def _reset(self) -> None:
        """

        """

        pass

########################################################################################################################

    def _set_counter(self) -> None:
        """
        Set the counter to the specified number of minutes. Count down second by second.
        """

        self._counter_time = datetime.now().replace(minute=0, second=self.PHASES[self._phase][self.TIME_KEY])
        self._update_counter()
        self._update_info()
        self._window.after(1000, self._count_down)

########################################################################################################################

    def _update_counter(self) -> None:
        """
        Update the counter time in the main window.
        """

        self._canvas.itemconfig(self._counter_label, text=self._counter_time.strftime("%M:%S"))

########################################################################################################################

    def _update_info(self) -> None:
        """
        Update the label which displays the name of the current pomodoro phase and the progress label.
        """

        self._info_label.configure(text=self.PHASES[self._phase][self.LABEL_KEY])
        self._progress_label.configure(text="\u2714" * self._phase)

########################################################################################################################

    def _count_down(self) -> None:
        """
        Subtract one second from the counter until it is on zero minutes and seconds.
        """

        self._counter_time -= timedelta(seconds=1)
        self._update_counter()

        if self._counter_time.minute != 0 or self._counter_time.second != 0:
            # counter above 00:00, continue
            self._window.after(1000, self._count_down)
        else:
            # counter reached 00:00, move to the next phase
            self._phase += 1
            self._phase %= len(self.PHASES)
            self._window.after(1000, self._set_counter)


########################################################################################################################

def run_program() -> None:
    """
    Run the Pomodoro application.
    """

    Pomodoro()


########################################################################################################################

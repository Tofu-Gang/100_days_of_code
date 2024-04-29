from tkinter import Tk, Canvas, PhotoImage, Label, Button
from os.path import join, dirname, realpath
from datetime import datetime, timedelta

from .pomodoro_engine import PomodoroEngine


########################################################################################################################

class Pomodoro:
    _BG_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), "tomato.png")
    _PINK = "#e2979c"
    _RED = "#e7305b"
    _GREEN = "#9bdeac"
    _YELLOW = "#f7f5dd"
    _COUNTER_FONT = ("Courier", 27, "bold")
    _INFO_FONT = ("Courier", 30, "bold")
    _WINDOW_PAD_X = 100
    _WINDOW_PAD_Y = 50

########################################################################################################################

    def __init__(self):
        """
        Set up the display widgets and window controls. Create the routine engine which controls the routine flow.
        Finally, show the main window.
        """

        self._engine = PomodoroEngine()
        self._set_display()
        self._set_controls()
        self._update()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """
        Create the main window with a background image. Set up the colors and geometry. Create the main info label above
        the tomato picture and progress label (checkmarks) between the buttons.
        """

        self._window = Tk()
        self._window.configure(padx=self._WINDOW_PAD_X, pady=self._WINDOW_PAD_Y, bg=self._YELLOW)

        # could be set as a local variable, but I guess the garbage collector deletes it and then the image won't get
        # displayed at all
        self._tomato_img = PhotoImage(file=self._BG_IMAGE_FILE_PATH)
        tomato_width = self._tomato_img.width()
        tomato_height = self._tomato_img.height()
        tomato_pos_x = tomato_width / 2
        # the image is cut on the bottom for some reason, subtract some pixels from the y positions to fix that
        tomato_pos_y = tomato_height / 2 - 1
        counter_label_pos_x = tomato_pos_x
        counter_label_pos_y = tomato_pos_y + 18

        self._canvas = Canvas(width=tomato_width, height=tomato_height, bg=self._YELLOW, highlightthickness=0)
        self._canvas.create_image(tomato_pos_x, tomato_pos_y, image=self._tomato_img)
        self._counter_label = self._canvas.create_text(counter_label_pos_x, counter_label_pos_y,
                                                       fill="white", font=self._COUNTER_FONT)
        self._canvas.grid(row=1, column=1)

        self._info_label = Label(bg=self._YELLOW, font=self._INFO_FONT)
        self._info_label.grid(row=0, column=1)
        self._progress_label = Label(fg=self._GREEN, bg=self._YELLOW)
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

        self._engine.start()
        self._set_counter()

########################################################################################################################

    def _reset(self) -> None:
        """
        Stop the pomodoro routine.
        """

        self._engine.reset()
        self._update()

########################################################################################################################

    def _set_counter(self) -> None:
        """
        Set the counter to the specified number of minutes. Count down second by second.
        """

        self._counter_time = datetime.now().replace(minute=self._engine.phase_duration, second=0)
        self._update()
        self._window.after(1000, self._count_down)

########################################################################################################################

    def _count_down(self) -> None:
        """
        Subtract one second from the counter. Control the pomodoro routine after the counter hits zero.
        """

        self._counter_time -= timedelta(seconds=1)
        self._update()

        if self._engine.is_running:
            if self._counter_time.minute != 0 or self._counter_time.second != 0:
                # counter above 00:00, continue
                self._window.after(1000, self._count_down)
            else:
                # counter reached 00:00, move to the next phase
                self._engine.next_phase()
                self._window.attributes('-topmost', 1)
                self._window.attributes('-topmost', 0)

                if self._engine.is_running:
                    self._window.after(1000, self._set_counter)
                else:
                    self._window.after(1000, self._update)

########################################################################################################################

    def _update(self) -> None:
        """
        Update the whole window.
        """

        if self._engine.is_running:
            self._canvas.itemconfig(self._counter_label, text=self._counter_time.strftime("%M:%S"))
            self._window.title(f"{self._engine.phase_label} {self._counter_time.strftime('%M:%S')}")
            self._info_label.configure(text=self._engine.phase_label,
                                       fg=self._GREEN if self._engine.is_work_phase else self._PINK)
        else:
            self._canvas.itemconfig(self._counter_label, text="")
            self._window.title(self._engine.phase_label)
            self._info_label.configure(text=self._engine.phase_label, fg=self._PINK)

        self._progress_label.configure(text="\u2714" * self._engine.work_phases_complete)


########################################################################################################################

def run_program() -> None:
    """
    Run the Pomodoro application.
    """

    Pomodoro()


########################################################################################################################

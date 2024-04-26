from tkinter import Tk, Label, Button, Entry


########################################################################################################################

class MilesToKms:
    WINDOW_WIDTH = 194
    WINDOW_HEIGHT = 108
    WINDOW_PADDING_X = 20
    WINDOW_PADDING_Y = 20

########################################################################################################################

    def __init__(self):
        """
        Create the window, set it up; create all the widgets, set them up; create a connection between the calculate
        button and a method that converts miles to kms.
        """

        self._window = Tk()
        self._miles_input = Entry(width=5)
        self._kms_label = Label(text="")
        self._calculate_button = Button(text="Calculate", command=self._calculate)
        self._setup_window()
        self._setup_layout()
        self._window.mainloop()

########################################################################################################################

    def _setup_window(self) -> None:
        """
        Set window size and padding.
        """

        self._window.title("Miles to Kilometers")
        self._window.minsize(width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self._window.maxsize(width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self._window.config(padx=self.WINDOW_PADDING_X, pady=self.WINDOW_PADDING_Y)

########################################################################################################################

    def _setup_layout(self) -> None:
        """
        Place all the widgets inside a grid.
        """

        Label(text="Miles").grid(row=0, column=2)
        Label(text="is equal to").grid(row=1, column=0)
        Label(text="Km").grid(row=1, column=2)
        self._miles_input.grid(row=0, column=1)
        self._kms_label.grid(row=1, column=1)
        self._calculate_button.grid(row=2, column=1)

########################################################################################################################

    def _calculate(self) -> None:
        """
        Convert miles to kms. Extract miles value from the input text line and show the result in a label.
        """

        try:
            self._kms_label.config(text="{:.1f}".format(float(self._miles_input.get()) * 1.609))
        except ValueError:
            # user did not enter a valid number
            pass


########################################################################################################################

def run_program() -> None:
    """
    Run the Miles to Kms converter.
    """

    MilesToKms()


########################################################################################################################

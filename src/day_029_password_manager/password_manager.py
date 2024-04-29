from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, END
from os.path import join, dirname, realpath


########################################################################################################################

class PasswordManager:
    _BG_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), "logo.png")
    _OUT_FILE_PATH = join(dirname(realpath(__file__)), "data.txt")
    _WINDOW_PADDING = 50
    _LOGO_WIDTH = 200
    _LOGO_HEIGHT = 200

########################################################################################################################

    def __init__(self):
        """

        """

        self._set_display()
        self._set_controls()
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
        self._canvas.grid(row=0, column=1)

        Label(text="Website:").grid(row=1, column=0)
        Label(text="Email/Username:").grid(row=2, column=0)
        Label(text="Password:").grid(row=3, column=0)

########################################################################################################################

    def _set_controls(self) -> None:
        """

        """

        self._website_entry = Entry()
        self._website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
        self._website_entry.focus()
        self._username_entry = Entry()
        self._username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
        self._username_entry.insert(0, "borts@bootus.com")
        self._password_entry = Entry()
        self._password_entry.grid(row=3, column=1, sticky="EW")
        Button(text="Generate Password", command=self._generate_password).grid(row=3, column=2)
        Button(text="Add", command=self._add_password).grid(row=4, column=1, columnspan=2, sticky="EW")

########################################################################################################################

    def _generate_password(self) -> None:
        """

        """

        pass

########################################################################################################################

    def _add_password(self) -> None:
        """

        """

        with open(self._OUT_FILE_PATH, "a") as f:
            f.write(f"{self._website_entry.get()} | {self._username_entry.get()} | {self._password_entry.get()}\n")

        self._website_entry.delete(0, END)
        self._password_entry.delete(0, END)
        self._website_entry.focus()


########################################################################################################################

def run_program() -> None:
    """

    """

    PasswordManager()


########################################################################################################################

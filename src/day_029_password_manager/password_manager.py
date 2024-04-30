from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, END, messagebox
from os.path import join, dirname, realpath
from random import randint
from pyperclip import copy

from utils import generate_password


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
        Create and show the main window.
        """

        self._set_display()
        self._set_controls()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """
        Create and set up the main window, the logo and the entry labels.
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
        Set up the website, username and password entries. Furthermore, create generate and add password buttons and
        connect them to their respective methods.
        """

        self._website_entry = Entry()
        self._website_entry.grid(row=1, column=1, sticky="EW")
        self._website_entry.focus()
        self._username_entry = Entry()
        self._username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
        self._username_entry.insert(0, "borts@bootus.com")
        self._password_entry = Entry()
        self._password_entry.grid(row=3, column=1, sticky="EW")
        Button(text="Search", command=self._search).grid(row=1, column=2, sticky="EW")
        Button(text="Generate Password", command=self._generate_password).grid(row=3, column=2)
        Button(text="Add", command=self._add_password).grid(row=4, column=1, columnspan=2, sticky="EW")

########################################################################################################################

    def _search(self) -> None:
        """

        """

        pass

########################################################################################################################

    def _generate_password(self) -> None:
        """
        Generate a random password and add it to the password entry. Copy it to the clipboard.
        """

        self._password_entry.delete(0, END)
        password = generate_password(letters_count=randint(8, 10),
                                     numbers_count=randint(2, 4),
                                     symbols_count=randint(2, 4))
        self._password_entry.insert(0, password)
        copy(password)

########################################################################################################################

    def _add_password(self) -> None:
        """
        Check if all three entries are not empty and that the user agrees with saving this entry to the output file.
        If all is ok, save the password entry to the output file and prepare the window for the next password.
        """

        if (len(self._website_entry.get()) == 0 or
                len(self._username_entry.get()) == 0 or
                len(self._password_entry.get()) == 0):
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        else:
            output_line = f"{self._website_entry.get()} | {self._username_entry.get()} | {self._password_entry.get()}\n"
            is_ok = messagebox.askyesno(title=self._website_entry.get(), message=f"These are the details entered: \n"
                                                                                 f"{output_line}\n"
                                                                                 f"Is it ok to save?")
            if is_ok:
                with open(self._OUT_FILE_PATH, "a") as f:
                    f.write(output_line)

                self._website_entry.delete(0, END)
                self._password_entry.delete(0, END)
                self._website_entry.focus()


########################################################################################################################

def run_program() -> None:
    """
    Run the password manager.
    """

    PasswordManager()


########################################################################################################################

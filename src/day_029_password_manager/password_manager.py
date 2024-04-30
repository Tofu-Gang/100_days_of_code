from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, END, messagebox
from os.path import join, dirname, realpath
from random import randint
from typing import Union

from pyperclip import copy, PyperclipException
from json import load, dump

from utils import generate_password


########################################################################################################################

class Database:
    _OUT_FILE_PATH = join(dirname(realpath(__file__)), "data.json")
    _USERNAME_KEY = "USERNAME"
    _PASSWORD_KEY = "PASSWORD"

########################################################################################################################

    def __init__(self):
        """
        Load password database from the data file.
        """

        try:
            with open(self._OUT_FILE_PATH, "r") as f:
                self._data = load(f)
        except FileNotFoundError:
            # no data file exists; create empty dictionary
            self._data = dict()

########################################################################################################################

    def add_data(self, website: str, username: str, password: str) -> None:
        """
        Add data to the database and save it to the data file.

        :param website: website name
        :param username: username/email
        :param password: password
        """

        self._data.update({
            website: {
                self._USERNAME_KEY: username,
                self._PASSWORD_KEY: password
            }
        })

        with open(self._OUT_FILE_PATH, "w") as f:
            dump(self._data, f, indent=4)

########################################################################################################################

    def data_exist(self, website: str) -> bool:
        """
        :param website: website name
        :return: True if data for the specified website exist, False otherwise
        """

        return website in self._data

########################################################################################################################

    def get_username(self, website: str) -> Union[str, None]:
        """
        :param website: website name
        :return: username for the website or None if the data do not exist
        """

        try:
            return self._data[website][self._USERNAME_KEY]
        except KeyError:
            return None

########################################################################################################################

    def get_password(self, website: str) -> Union[str, None]:
        """
        :param website: website name
        :return: password for the website or None if the data do not exist
        """

        try:
            return self._data[website][self._PASSWORD_KEY]
        except KeyError:
            return None


########################################################################################################################

class PasswordManager:
    _BG_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), "logo.png")
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
        self._database = Database()
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
        Search the database for data from specified website. Show it in a messagebox if it exists, or tell the user
        via a messagebox that the data for this website do not exist.
        """

        website = self._website_entry.get()

        if len(website) == 0:
            messagebox.showinfo(title="Oops", message="Website field is empty!")
        elif self._database.data_exist(website):
            username = self._database.get_username(website)
            password = self._database.get_password(website)
            messagebox.showinfo(title=website, message=f"Data found:\nUsername: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No data found for {website}.")

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

        try:
            # copy the password to clipboard
            copy(password)
        except PyperclipException:
            # Pyperclip could not find a copy/paste mechanism for your system.
            # For more information, please visit
            # https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error
            pass

########################################################################################################################

    def _add_password(self) -> None:
        """
        Check if all three entries are not empty and that the user agrees with saving this entry to the output file.
        If all is ok, save the password entry to the output file and prepare the window for the next password.
        """

        website = self._website_entry.get()
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(website) == 0 or len(username) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        else:
            if self._database.data_exist(website):
                is_ok = messagebox.askyesno(
                    title=website,
                    message=f"Data already exist:\n"
                            f"Username: {self._database.get_username(website)}\n"
                            f"Password: {self._database.get_password(website)}\n"
                            f"New data:\n"
                            f"Username: {username}\n"
                            f"Password: {password}\n"
                            f"Overwrite?")
            else:
                is_ok = messagebox.askyesno(
                    title=website,
                    message=f"These are the details entered:\n"
                            f"{website}\n"
                            f"Username: {username}\n"
                            f"Password: {password}\n"
                            f"Is it ok to save?")
            if is_ok:
                self._database.add_data(website, username, password)
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

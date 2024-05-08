from tkinter import Tk, Canvas, PhotoImage, Button
from os.path import join, realpath, dirname
from requests import get


########################################################################################################################

class Kanye:
    _BG_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), "img", "background.png")
    _KANYE_IMAGE_FILE_PATH = join(dirname(realpath(__file__)), "img", "kanye.png")

########################################################################################################################

    def __init__(self):
        """
        Create the window and one control button. Generate initial quote.
        """

        self._set_display()
        self._set_controls()
        self._get_quote()
        self._window.mainloop()

########################################################################################################################

    def _set_display(self) -> None:
        """
        Create the window with a canvas to display a quote text. Set up geometry and quote font.
        """

        self._window = Tk()
        self._window.title("Kanye Says...")
        self._window.config(padx=50, pady=50)

        self._background_img = PhotoImage(file=self._BG_IMAGE_FILE_PATH)
        self._canvas = Canvas(width=300, height=414)
        self._canvas.create_image(150, 207, image=self._background_img)
        self._canvas.grid(row=0, column=0)
        self._quote_text = self._canvas.create_text(150, 207, width=250, font=("Arial", 30, "bold"), fill="white")

########################################################################################################################

    def _set_controls(self) -> None:
        """
        Create a button which is used to fetch and display a Kanye West quote.
        """

        self._kanye_img = PhotoImage(file=self._KANYE_IMAGE_FILE_PATH)
        Button(image=self._kanye_img, highlightthickness=0, command=self._get_quote).grid(row=1, column=0)

########################################################################################################################

    def _get_quote(self) -> None:
        """
        Fetch a Kanye West quote from the API. Display it in the canvas.
        """

        response = get(url="https://api.kanye.rest")
        response.raise_for_status()
        self._canvas.itemconfig(self._quote_text, text=response.json()["quote"])


########################################################################################################################

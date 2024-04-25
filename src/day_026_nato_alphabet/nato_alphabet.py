from os.path import join, dirname, realpath
from typing import Tuple
from pandas import read_csv


########################################################################################################################
class NatoAlphabet:
    NATO_ALPHABET_FILE_NAME = "nato_phonetic_alphabet.csv"
    NATO_ALPHABET_FILE_PATH = join(dirname(realpath(__file__)), NATO_ALPHABET_FILE_NAME)
    LETTER_COLUMN = "letter"
    CODE_COLUMN = "code"

########################################################################################################################

    def __init__(self):
        """
        Read NATO alphabet from csv file and save it as a dict where keys are alphabet letters and values are codes for
        respective letters.
        """

        self._nato_alphabet = {
            row[self.LETTER_COLUMN]: row[self.CODE_COLUMN]
            for (index, row) in read_csv(self.NATO_ALPHABET_FILE_PATH).iterrows()
        }

########################################################################################################################

    def _get_letter_code(self, letter: str) -> str:
        """
        :param letter: a letter
        :return: a corresponding code from the NATO alphabet or None if there is no code for the input
        """

        return self._nato_alphabet[letter.upper()]

########################################################################################################################

    def get_word_codes(self, word: str) -> Tuple[str, ...]:
        """
        :param word: an input word we want to spell with codes from the NATO alphabet
        :return: a tuple of NATO codes for each letter from the input word
        """

        return tuple(self._get_letter_code(letter) for letter in word)


########################################################################################################################

def run_program() -> None:
    """
    Get a word from the user. Print NATO alphabet codes for each letter of the word.
    """

    word = input("Enter a word: ")
    nato_alphabet = NatoAlphabet()
    print(", ".join(nato_alphabet.get_word_codes(word)))

########################################################################################################################

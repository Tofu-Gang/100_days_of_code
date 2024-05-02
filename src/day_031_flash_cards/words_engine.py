from os.path import join, dirname, realpath
from random import choice
from pandas import read_csv


########################################################################################################################

class Word:

    def __init__(self, original: str, translation: str):
        """
        Create a word which has its original form and translated form.

        :param original: the original form of the word
        :param translation: the translated form of the word
        """

        self._original = original
        self._translation = translation

########################################################################################################################

    @property
    def original(self) -> str:
        """
        :return: the original form of the word
        """

        return self._original

########################################################################################################################

    @property
    def translation(self) -> str:
        """
        :return: the translated form of the word
        """

        return self._translation


########################################################################################################################

class WordsEngine:
    _WORDS_FILE_PATH = join(dirname(realpath(__file__)), "data", "words.csv")

########################################################################################################################

    def __init__(self):
        """
        Load words from a data file and transform it so the database can be easily used by the GUI.
        """

        frame = read_csv(self._WORDS_FILE_PATH)
        self._original_lang = frame.columns[0]
        self._translation_lang = frame.columns[1]
        self._words = tuple(Word(entry[self._original_lang], entry[self._translation_lang])
                            for entry in frame.to_dict(orient="records"))

########################################################################################################################

    @property
    def original_lang(self) -> str:
        """
        :return: original language of the words
        """

        return self._original_lang

########################################################################################################################

    @property
    def translation_lang(self) -> str:
        """
        :return: language the words are translated into
        """

        return self._translation_lang

########################################################################################################################

    def get_random_word(self) -> Word:
        """
        :return: random word
        """

        return choice(self._words)

########################################################################################################################

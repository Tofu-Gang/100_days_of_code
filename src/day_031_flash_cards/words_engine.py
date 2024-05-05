from os.path import join, dirname, realpath
from random import choice
from pandas import read_csv, DataFrame


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
    _WORDS_ORIGINAL_FILE_PATH = join(dirname(realpath(__file__)), "data", "words.csv")
    _WORDS_FILE_PATH = join(dirname(realpath(__file__)), "data", "words_to_learn.csv")

########################################################################################################################

    def __init__(self):
        """
        Load words from a data file and transform it so the database can be easily used by the GUI.
        """

        try:
            # load only the words the user still needs to learn
            frame = read_csv(self._WORDS_FILE_PATH)
        except FileNotFoundError:
            # if that file does not exist, load all words
            frame = read_csv(self._WORDS_ORIGINAL_FILE_PATH)

        self._original_lang = frame.columns[0]
        self._translation_lang = frame.columns[1]
        self._words = list(Word(entry[self._original_lang], entry[self._translation_lang])
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

    def remove_word(self, word: Word) -> None:
        """
        Remove a word from the database. This means that the user knows the word and no longer needs to learn it.

        :param word: Word to be removed from the database
        """

        self._words.remove(word)

########################################################################################################################

    def save_words(self) -> None:
        """
        Save the words that the user still needs to learn to a file.
        """

        DataFrame({
            self._original_lang: list(word.original for word in self._words),
            self._translation_lang: list(word.translation for word in self._words)
        }).to_csv(self._WORDS_FILE_PATH, index=False)

########################################################################################################################

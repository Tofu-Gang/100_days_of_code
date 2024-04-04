from random import shuffle
from typing import Union


########################################################################################################################

class Deck52Standard:
    """
    A standard 52 cards deck represented only by the cards' values. Cards 2-10 count as their rank, the jack, queen and
    king count as 10 and aces count as 11. The deck can be reset (by returning all drawn cards back to it) and shuffled.
    First card from the deck can be drawn (which removes the card from the deck).
    """

    def __init__(self):
        """
        Create the deck with all the 52 cards in it.
        """

        self._deck = []
        self._reset()

########################################################################################################################

    def _reset(self) -> None:
        """
        Return all the drawn cards back to the deck.
        """

        self._deck = 4 * (list(range(2, 12)) + 3 * [10])

########################################################################################################################

    def shuffle(self) -> None:
        """
        Shuffle the deck of cards.
        """

        self._reset()
        shuffle(self._deck)

########################################################################################################################

    def draw(self) -> Union[int, None]:
        """
        :return: first card from the deck (it is removed from the deck as well)
        """

        if len(self._deck) > 0:
            card = self._deck[0]
            self._deck = self._deck[1:]
            return card

########################################################################################################################

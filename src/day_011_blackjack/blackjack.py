from src.day_011_blackjack.deck import Deck52Standard
from utils import clear_screen


class Blackjack:
    LOGO = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

########################################################################################################################

    def __init__(self):
        """
        Initialize the game of Blackjack. Get a brand-new standard 52 cards deck and make place for player and dealer
        cards.
        """

        self._deck = Deck52Standard()
        self._player_cards = []
        self._dealer_cards = []

########################################################################################################################

    def _get_player_action(self) -> str:
        """
        :return: either "h", "hit", "s" or "stand"
        """

        while True:
            print("Type \"(h)it\" or \"(s)tand\" to get another card or pass:")
            player_action = input("> ").strip().lower()

            if player_action in ("h", "hit", "s", "stand"):
                return player_action
            else:
                print("Invalid value. Please try again.")

########################################################################################################################

    def _is_player_bust(self) -> bool:
        """
        :return: True if total value of player cards is over 21, False otherwise
        """

        return sum(self._player_cards) > 21

########################################################################################################################

    def _is_dealer_bust(self) -> bool:
        """
        :return: True if total value of dealer cards is over 21, False otherwise
        """

        return sum(self._dealer_cards) > 21

########################################################################################################################

    def _is_blackjack(self) -> bool:
        """
        :return: True if total value of player cards is exactly 21, False otherwise
        """

        return sum(self._player_cards) == 21

########################################################################################################################

    def _does_player_stand(self) -> bool:
        """
        :return: True if the player does not wish to draw more cards anymore, False otherwise
        """

        return len(self._dealer_cards) > 1

########################################################################################################################

    def _finish_dealer_draw(self) -> None:
        """
        Draw cards for the dealer until sum of their cards is 17 or more.
        """

        while sum(self._dealer_cards) < 17:
            self._dealer_cards.append(self._deck.draw())

########################################################################################################################

    def new_game(self) -> None:
        """
        Play the game of Blackjack.
        """

        print(self.LOGO)
        self._player_cards.clear()
        self._dealer_cards.clear()
        self._deck.shuffle()

        self._player_cards.append(self._deck.draw())
        self._dealer_cards.append(self._deck.draw())
        self._player_cards.append(self._deck.draw())

        while True:
            if self._does_player_stand():
                print(f"Your final hand: {self._player_cards}, score: {sum(self._player_cards)}")
                print(f"Dealer final hand: {self._dealer_cards}, score: {sum(self._dealer_cards)}")

                if self._is_dealer_bust():
                    print("Dealer bust! You win.")
                elif sum(self._player_cards) > sum(self._dealer_cards):
                    print("Your score is higher than the dealer's! You win.")
                elif sum(self._player_cards) < sum(self._dealer_cards):
                    print("Your score is lower than the dealer's! You lose.")
                else:
                    print("Your score is equal to the dealer's! Draw.")
                break
            else:
                print(f"Your cards: {self._player_cards}, current score: {sum(self._player_cards)}")
                print(f"Dealer's first card: {self._dealer_cards[0]}")

                if self._is_player_bust():
                    print("Bust! You lose.")
                    break
                elif self._is_blackjack():
                    print("Blackjack! You win.")
                    break
                else:
                    player_action = self._get_player_action()

                    if player_action in ("h", "hit"):
                        self._player_cards.append(self._deck.draw())
                    elif player_action in ("s", "stand"):
                        self._finish_dealer_draw()

        print("Press Enter to continue or Ctrl+C to exit.")
        input()
        clear_screen()
        self.new_game()


########################################################################################################################

def run_program() -> None:
    """
    Play the game of Blackjack.
    """

    blackjack = Blackjack()
    blackjack.new_game()

########################################################################################################################

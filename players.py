"""
This module contains the Player and Dealer definitions and moves.
"""

from random import randrange

from python_terminal_color import color
from cards import Face


def _random_line(file):
    line = next(file)
    for i, line in enumerate(file, 2):
        if randrange(i):
            continue
        res = line
    return res


class Player():
    """
    An interactive Player with a hand.
    Shares a deck with other players and dealers.
    """
    deck = None

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.finished = False

    def move(self):
        """Process player moves, prompting for action."""
        if self.finished:
            return

        while self.has_ace() and self.score() > 21:
            for card in self.hand:
                # flip aces, as needed
                if card.value == 11:
                    card.value = 1
                    break

        # show the player their state
        self.print_hand()

        # check victory/loss conditions
        if self.score() == 21:
            self.finished = True
            return

        if self.score() > 21:
            # print("Busted!")
            self.finished = True
            return

        # process user input
        hit_or_stay = input(
                f"{self.name}, what would you like to do?\n([H]it|[S]tay) > "
                ) + " "
        while hit_or_stay[0].casefold() not in {"h", "s"}:
            hit_or_stay = input("Try again. > ") + " "
        if hit_or_stay[0].casefold() == "h":
            self.hit()
        else:
            self.finished = True

    def hit(self):
        """Add a card from the deck to the player's hand."""
        self.hand.append(self.deck.pop())

    def score(self):
        """Return the player's score."""
        return sum(card.value for card in self.hand)

    def print_hand(self):
        """Prints the player's hand and score."""
        print(f"{self.name}'s hand:")
        print(
                color.white_bg(" ").join(
                    str(card) for card in self.hand
                    ), end=color.white_bg(" \n")
                )
        print(f"{self.name}'s score: {self.score()}")
        print()

    def has_ace(self):
        """Check if the Player has an Ace."""
        return any(card.value == 11 for card in self.hand)


class Dealer(Player):
    """
    A non-interactive player with a hand.
    Shares a deck with other players and dealers.
    """
    def __init__(self, hand, name=None):
        if name is None:
            try:
                with open("names_d.txt", mode="rt") as names:
                    name = "{} the Dealer".format(_random_line(names).strip())
            except OSError:
                name = "Donnie the Dealer"
        super().__init__(name, hand)

    def move(self):
        """Process dealer moves, automatically."""
        while self.score() < 17:
            self.hit()
        if self.has_ace() and self.score() == 17:
            self.hit()
        while self.has_ace() and self.score() > 21:
            for card in self.hand:
                if card.value == 11:
                    card.value = 1
                    self.move()
                    break
        self.finished = True


class Computer(Dealer):
    """
    A non-interactive player with a hand.
    Shares a deck with other players and dealers.
    """
    def __init__(self, hand, name=None):
        if name is None:
            try:
                with open("names_c.txt", mode="rt") as names:
                    name = "{} the Computer".format(
                            _random_line(names).strip()
                            )
            except OSError:
                name = "Karen the Computer"
        super().__init__(hand, name)

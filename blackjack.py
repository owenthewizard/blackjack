#!/usr/bin/env python3

"""
Implements the U.S. version of blackjack.
"""

from random import shuffle

import readline

from python_terminal_color import color
from cards import Card, Deck
from players import Computer, Dealer, Player


# https://stackoverflow.com/a/8505387/5819375
def _input_prefill(prompt, text):
    """Like input(), but with text already filled in."""
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


class Blackjack():
    """It's blackjack!"""
    def __init__(self):
        print("The game is blackjack gentlemen.")

        self.humans_num = _input_prefill(
            "How many players do we have tonight?\n> ",
            "1"
        )
        while not self.humans_num.isdigit():
            self.humans_num = input("Try again. > ")

        self.humans = set()
        for i in range(1, int(self.humans_num) + 1):
            name = _input_prefill(
                "What's your name, son?\n> ",
                f"Player {i}"
            )
            self.humans.add(name)

        self.computers = _input_prefill(
            "How many computers will be playing with us?\n> ",
            "1"
        )
        while not self.computers.isdigit():
            self.computers = input("Try again. > ")
        self.computers = int(self.computers)

        self.decks = _input_prefill(
            "How many decks would you like to play with tonight?\n> ",
            "1"
        )
        while not self.decks.isdigit() or int(self.decks) == 0:
            self.decks = input("Try again. > ")
        self.decks = int(self.decks)

        self.reset()

    def play(self):
        """Play blackjack!"""
        while not all(player.finished for player in self.players):
            for player in self.players:
                player.move()
        self.dealer.move()

    def finish(self):
        """Finish the game and tally the score."""
        self.dealer.print_hand()
        for player in self.players:
            player.print_hand()
            if player.score() == 21 and len(player.hand) == 2:
                print(f"Congratulations {player.name}, you're a natural!", end="\n\n")
            elif player.score() <= 21:
                if self.dealer.score() > 21:
                    print(f"{self.dealer.name} busted! Great job {player.name}!", end="\n\n")
                elif player.score() > self.dealer.score():
                    print(f"{player.score()} beats {self.dealer.score()}. Congratulations {player.name}!", end="\n\n")
                elif player.score() < self.dealer.score():
                    print(f"{self.dealer.score()} beats {player.score()}. Too bad {player.name}!", end="\n\n")
                else:
                    print(f"Push, it's a tie! Not bad {player.name}!", end="\n\n")
            else:
                print(f"{player.name}, you got busted!", end="\n\n")

    def reset(self):
        """Resets the game state so we can play again."""
        self.deck = Deck.standard()
        for _ in range(1, self.decks):
            self.deck.extend(Deck.standard())
        shuffle(self.deck)
        # initializes the deck for Computers, Dealers, and Players
        Player.deck = self.deck

        self.players = [
            Player(name, [self.deck.pop()]) for name in self.humans
        ]
        self.players.extend([
            Computer(
                [self.deck.pop()]
            ) for _ in range(int(self.computers))
        ])

        # dealer starts with two cards, one flipped over
        dealer_card = self.deck.pop()
        fake_card = Card(
            0, None, None, 0x1F0A0,
            lambda x: color.white_bg(color.black(x))
        )
        self.dealer = Dealer([fake_card, self.deck.pop()])
        self.dealer.print_hand()
        self.dealer.hand[0] = dealer_card


if __name__ == "__main__":
    game = Blackjack()
    game.play()
    game.finish()

    try:
        while input(
            "Would you like to play again?\n(y/N) > "
        ).casefold()[0] == 'y':
            game.reset()
            game.play()
            game.finish()
    except IndexError:
        pass
    except (EOFError, KeyboardInterrupt):
        print()

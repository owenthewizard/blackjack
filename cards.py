"""
This module contains definitions for Card and Deck, as well as enums
for Suit and Face. This allows for the creation and manipulation of
cards.
"""


from enum import IntEnum

from python_terminal_color import color as colors


def _nop(*args):
    """A simple nop, to be used as color=None"""
    return args[0]


class Suit(IntEnum):
    """Represents the four possible Card suits."""
    SPADES      = 0xA0  # noqa: E221
    HEARTS      = 0xB0  # noqa: E221
    DIAMONDS    = 0xC0  # noqa: E221
    CLUBS       = 0xD0  # noqa: E221


class Face(IntEnum):
    """Represents the three possible Card faces, as well as Ace."""
    ACE         = 0x01  # noqa: E221
    JACK        = 0x0B  # noqa: E221
    QUEEN       = 0x0D  # noqa: E221
    KING        = 0x0E  # noqa: E221


class Card():
    """
    Represents a Pip or Face card with a value, suit, and unicode
    codepoint.
    """
    def __init__(self, value, face, suit, unicode, color=_nop):
        self.value = value
        self.face_ = face
        self.suit = suit
        self.unicode = unicode
        self.color = color

    @classmethod
    def face(cls, face, suit, color=_nop):
        """Create a face card with a suit."""
        # face cards are always valued at 10
        # except for the special caase of Ace
        value = 11 if face is Face.ACE else 10
        unicode = 0x1F000 + suit + face
        return cls(value, face, suit, unicode, color)

    @classmethod
    def pip(cls, value, suit, color=_nop):
        """Create a pip card with a value and suit."""
        unicode = 0x1F000 + suit + value
        return cls(value, None, suit, unicode, color)

    def __str__(self):
        return self.color(chr(self.unicode))

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other


class Deck(list):
    """
    A deck of cards, usually used as a stack.
    Currently implemented as a list.
    """
    @classmethod
    def standard(cls):
        """Create a standard 52-card deck"""
        red = lambda x: colors.white_bg(colors.red(x))  # noqa: E731
        black = lambda x: colors.white_bg(colors.black(x))  # noqa: E731
        color = lambda x: red if (  # noqa: E731
                x is Suit.HEARTS or x is Suit.DIAMONDS
                ) else black
        pips = (Card.pip(n, s, color(s)) for n in range(2, 11) for s in Suit)
        faces = (Card.face(f, s, color(s)) for f in Face for s in Suit)
        deck = list(pips) + list(faces)
        return cls(deck)

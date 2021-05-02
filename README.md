# blackjack.py

A simple game of blackjack I made for fun.

Implemented as per the rules on [Wikipedia](https://en.wikipedia.org/wiki/Blackjack#Rules)

> - If the player is dealt an Ace and a ten-value card (called a "blackjack" or "natural"), and the dealer does not, the player wins and usually receives a bonus.
> - If the player exceeds a sum of 21 ("busts"), the player loses, even if the dealer also exceeds 21.
> - If the dealer exceeds 21 ("busts") and the player does not, the player wins.
> - If the player attains a final sum higher than the dealer and does not bust, the player wins.
> - If both dealer and player receive a blackjack or any other hands with the same sum, this will be called a "push" and no one wins.

## Quick Start

Clone this repo and run [blackjack.py](blackjack.py).

## """Screenshots"""

```
The game is blackjack gentlemen.
How many players do we have tonight?
> 1
What's your name, son?
> Owen
How many computers will be playing with us?
> 2
How many decks would you like to play with tonight?
> 1
Dorothy the Dealer's hand:
🂠 🂣
Dorothy the Dealer's score: 3

Owen's hand:
🃑
Owen's score: 11

Owen, what would you like to do?
([H]it|[S]tay) > h
Owen's hand:
🃑 🂩
Owen's score: 20

Owen, what would you like to do?
([H]it|[S]tay) > s
Dorothy the Dealer's hand:
🃈 🂣 🃘
Dorothy the Dealer's score: 19

Owen's hand:
🃑 🂩
Owen's score: 20

20 beats 19. Congratulations Owen!

Campbell the Computer's hand:
🂦 🂵 🂧
Campbell the Computer's score: 18

19 beats 18. Too bad Campbell the Computer!

Calla the Computer's hand:
🃒 🂸 🂫
Calla the Computer's score: 20

20 beats 19. Congratulations Calla the Computer!

Would you like to play again?
(y/N) >
```

## Features

- Automatic computer players
- Multiple human players
- Unicode card representations
- Color console support

## Missing Features / Issues

- There's currently no support for betting (including double and surrender) or splitting.
- [blackjack.py](blackjack.py) depends on readline.
  The readline functionality isn't critical, if you really want to run it on Windows you can just patch it out.
- The prompts currently assume the player is male. I'm keeping it as is for now because I appreciate the cabaret tone.
  Feel free to submit a PR if you have a suggestion. The prompts may be edited in [blackjack.py](blackjack.py).

### Coding Style

Obey [PEP 8](https://pep8.org) (via [flake8](https://flake8.pycqa.org/en/latest/)) and more (via [pylint](https://pylint.org/))

## Acknowledgments

- [python-terminal-color](https://github.com/reorx/python-terminal-color) by Xiao Meng @reorx.

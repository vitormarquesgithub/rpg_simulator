import random
from assets.terminal_colors import gray
from assets.terminal_colors import blue
from assets.terminal_colors import yellow

def roll(dice):
    result = random.randint(1, dice.faces)
    return print(gray('You rolled a ') + blue(dice.name) + gray(': ') + yellow(result))



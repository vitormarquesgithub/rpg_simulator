import random
from core.dices import Dice

def Roll(dice):
    result = random.randint(1, dice.faces)
    return print(f'You rolled a {dice.name}: {result}')



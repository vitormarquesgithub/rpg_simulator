import random

def roll(dice):
    result = random.randint(1, dice.faces)
    return print(f'You rolled a {dice.name}: {result}')



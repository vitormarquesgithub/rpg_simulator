from core.validation import Validate_initial_option
from core.validation import Validate_end_option
from assets.colors import Terminal
from core.roll import Roll

def Menu():
    print('')
    print('_'*50)
    print('')
    print('1. D3')
    print('_'*50)
    print('')
    dice = ''
    while dice == '':
        dice_option = input(Terminal.Gray('Selec a dice: '))
        dice = Validate_initial_option(dice_option)
    print('')
    Roll(dice)
    End_menu(dice)

def End_menu(dice):
    print('')
    print('_'*50)
    print('')
    print('1. Roll again')
    print('2. Select dice')
    print('3. Quit')
    print('_'*50)
    print('')
    while True:
        end_option = input(Terminal.Gray('Selec a option: '))
        end_option_validate = Validate_end_option(end_option)
        if end_option_validate == 3:
            print('')
            return
        elif end_option_validate == 2:
            Menu()
        elif end_option_validate == 1:
            Roll(dice)
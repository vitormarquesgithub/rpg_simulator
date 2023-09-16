from core.validation import validate_initial_option
from core.validation import validate_end_option
from assets.terminal_colors import gray
from core.roll import roll

def menu(): 
    print('')
    print('_'*50)
    print('')
    print('1. D4')
    print('2. D6')
    print('3. D8')
    print('4. D10')
    print('5. D12')
    print('6. D20')
    print('_'*50)
    print('')
    dice = ''
    while dice == '': 
        dice_option = input(gray('Selec a dice: '))
        dice = validate_initial_option(dice_option)
    print('')
    roll(dice)
    end_menu(dice)

def end_menu(dice):
    print('')
    print('_'*50)
    print('')
    print('1. Roll again')
    print('2. Select dice')
    print('3. Quit')
    print('_'*50)
    print('')
    while True:
        end_option = input(gray('Selec a option: '))
        end_option_validate = validate_end_option(end_option)
        if end_option_validate == 3:
            print('')
            break
        elif end_option_validate == 2:
            menu()
            break
        elif end_option_validate == 1:
            roll(dice)
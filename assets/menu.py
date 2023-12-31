from utils.validation import validate_initial_option
from utils.validation import validate_end_option
from assets.terminal_colors import gray
from assets.terminal_colors import purple
from assets.terminal_colors import blue
from assets.terminal_colors import red
from dices.roll import roll

def menu(): 
    print('')
    print(gray('_'*50))
    print('')
    print(purple(' '*18 + 'DICES OPTIONS'))
    print(gray('_'*50))
    print('')
    print(purple('1. ') + blue('D4'))
    print(purple('2. ') + blue('D6'))
    print(purple('3. ') + blue('D8'))
    print(purple('4. ') + blue('D10'))
    print(purple('5. ') + blue('D12'))
    print(purple('6. ') + blue('D20'))
    print(purple('7. ') + red('Exit'))
    print(gray('_'*50))
    print('')
    dice = ''
    while dice == '': 
        dice_option = input(gray('Selec a dice: '))
        dice = validate_initial_option(dice_option)
    if dice_option == '7':
        return
    end_menu(dice)

def end_menu(dice):
    print(gray('_'*50))
    print('')
    print(purple('1. ') + blue('Roll again'))
    print(purple('2. ') + blue('Select dice'))
    print(purple('3. ') + red('Exit'))
    print(gray('_'*50))
    print('')
    roll(dice)
    print('')
    while True:
        end_option = input(gray('Selec a option: '))
        print('')
        end_option_validate = validate_end_option(end_option)
        if end_option_validate == 3:
            break
        elif end_option_validate == 2:
            menu()
            break
        elif end_option_validate == 1:
            roll(dice)
            print('')
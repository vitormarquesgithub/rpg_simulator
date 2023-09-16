from core.dices import dices_list
from assets.terminal_colors import red

def validate_initial_option(value): 
    str_value = str(value)
    if str_value.isnumeric():
        int_value = int(value)
        for i in range(0, len(dices_list)):
            if int_value == dices_list[i].id:
                return dices_list[i]
    not_found_print()
    return ''

def validate_end_option(value): 
    str_value = str(value)
    if str_value.isnumeric():
        int_value = int(value)
        if int_value == 1 or int_value == 2 or int_value == 3:
            return int_value
    not_found_print()
    return ''
    
def not_found_print():
    print('')
    print(red('Not found option'))
    print('')
from core.dices import dices_list

def Validate_initial_option(value): 
    str_value = str(value)
    if str_value.isnumeric():
        int_value = int(value)
        for i in range(0, len(dices_list)):
            if int_value == dices_list[i].id:
                return dices_list[i]
    print('not found')
    return ''

def Validate_end_option(value): 
    str_value = str(value)
    if str_value.isnumeric():
        int_value = int(value)
        if int_value == 1 or int_value == 2 or int_value == 3:
            return int_value
        else:
            print('not found')
            return ''
    
import main
import conts

def return_menu():
    print(conts.JUMP_LINE)
    inp = input(conts.QUESTION_RET)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(conts.JUMP_LINE)
        print(conts.RETURN_MENU)
    elif inp == 'n':
        exit_program()
        exit()
    else:
        error_menu()

def exit_program():
    print(conts.JUMP_LINE)
    print(conts.EXIT)

def error_menu():
    print(conts.JUMP_LINE)
    print(conts.ERR)
    print(conts.JUMP_LINE)
    print(conts.RETURN_MENU)
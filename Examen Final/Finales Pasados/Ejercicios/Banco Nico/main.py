from clients import Client
from bank import *
import conts
from file import file_initialize
import functions as ft

def main():
    bank = Bank()
    file_initialize()
    while True:
        print(conts.MAIN_INP)
        inp = input("")
        if inp == '1':
            client_name = str(input(conts.NAME))
            client_lastname = str(input(conts.LASTNAME))
            client_idnumber = str(input(conts.ID_NUMBER))
            client = Client(client_name, client_lastname, client_idnumber)
            bank.clients_append(client)
            ft.return_menu()
        elif inp == '2':
            bank.show_queue()
            ft.return_menu()
        elif inp == '3':
            bank.show_cls_treated()
            ft.return_menu()
        elif inp == '4':
            bank.treat_client()
            ft.return_menu()  
        elif inp == '5':
            bank.load_data()
            ft.return_menu()
        elif inp == '6':
                ft.exit_program()
                break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()
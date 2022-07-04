from author import Author
from book import Book
from client import Client
from function import Function
from main_option import *


class Menu():

    def main():
        f = Function()

        while True:
            print(MAIN_OPTION_TEXT)

            opc = int(input("Ingrese una opcion: "))

            if opc == 1:
                nombre = (input("Ingrese el nombre: "))
                nacionalidad = (input("Ingrese el nacionalidad: "))
                client = Client(nombre, nacionalidad)
                f.addClient(client)
                input("Ingrese una tecla para continuar...")

            elif opc == 2:
                nombre_libro = (input("Ingrese el nombre: "))
                tipo = (input("Ingrese el tipo: "))
                editorial = (input("Ingrese el editorial: "))
                año = (input("Ingrese el año: "))
                autor = (input("Ingrese el Autor: "))
                book = Book(nombre_libro, tipo, editorial, año, autor)
                f.addBook(book)
                input("Ingrese una tecla para continuar...")

            elif opc == 3:
                f.addClient(Client(input("Ingrese el nombre: "), input("Ingrese el apellido: ")))
                input("Ingrese una tecla para continuar...")

            elif opc == 4:
                f.viewBook()
                input("Ingrese una tecla para continuar...")

            elif opc == 5:
                f.viewClient()
                input("Ingrese una tecla para continuar...")
                
            elif opc == 6:
                break

if __name__ == "__main__":
    Menu.main()
from Libro import *
from Client import *
from Biblioteca import *
from Constantes import *

biblioteca = Biblioteca()

def menu():
    print("")

while True:
    menu()
    print(MAIN_OPTION_TEXT)
    optionMenu = input("Opcion: ")
    if optionMenu == "1":
        name = input("Ingrese el nombre del cliente: ")
        cliente = Cliente(name)
        biblioteca.AddClient(cliente)

    elif optionMenu == "2":
        name = input("Ingrese el nombre del libro ")
        tipo = input("Ingrese el tipo de libro ")
        editorial = input("Ingrese la editorial ")
        año = input("Ingrese año de lanzamiento ")
        autor = input("Ingrese el autor del libro ")
        libro = Libro(name, tipo, editorial, año, autor)
        biblioteca.AddBook(libro)

    elif optionMenu == "3":
        name = input("Ingrese el nombre del cliente a asignar el libro ")
        cliente = biblioteca.SearchClient(name)
        nameBook = input("Ingrese el nombre del libro a asignar al cliente ")
        libro = biblioteca.SearchBook(nameBook)
        biblioteca.Assign(cliente, libro)


    elif optionMenu == "0":
        print("Saliendo...")
        break
    else:
        print("Ha elegido una respuesta incorrecta")
        
from book import Book
from client import Client
from library import Library


print('Bienvenidos a la Biblioteca Virtual de la Universidad de Mendoza')
print('''
        -------------------------------------
        |       Seleccione una opcion       |
        | 1) Agregar libros                 |
        | 2) Agregar clientes               |
        | 3) Ver libros                     |
        | 4) Ver clientes                   |
        | 5) Prestar libro/s                |
        | 6) Salir del programa             |
        -------------------------------------  
            ''')


library = Library()

class Menu():

    def menu():
        l = library
        while True:
            
            opc = int(input('Ingrese la opcion requerida: '))

            if (opc == 1):
                name = input("Ingrese el nombre del libro: ")
                author = int(input("Ingrese la puntuacion del libro: "))
                isb = input("Ingrese el ISB del libro: ")
                book = Book(name, author, isb)
                library.AddBook(book)

            elif (opc == 2):
                name = input("Ingrese el nombre del cliente nuevo: ")
                client = library.AddClient(name)

            elif (opc == 3):
                book = Library.ShowBooks()
                l.ShowBooks()

            #elif (opc ==3):
        #name = input("Ingrese el nombre del cliente a asignar el libro ")
        #cliente = biblioteca.SearchClient(name)
        #nameBook = input("Ingrese el nombre del libro a asignar al cliente ")
        #libro = biblioteca.SearchBook(nameBook)
        #biblioteca.Assign(cliente, libro)
            
            #elif (opc == 4):

            elif (opc == 5):
                client = library.SearchClient(name)
                book = input("Ingrese el libro a prestar: ")
                l.AddBorrowed(book)

            elif (opc == 6):
                exit(print("""Gracias por usar este programa
            Un trabajo realizado por Lucas Galdame"""))

            else:
                print("La opcion ingresada es incorrecta")

    menu()
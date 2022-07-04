from clear import Clear
from author import Author
from book import Book
from reader import Reader
from library import Library


class Main(): 
    def main():
        l = Library()
        while True:
            Clear.clear()
            print("\n")
            print("Seleccione una opción: ")
            print("1. Agregar Autor.")
            print("2. Agregar Libro.")
            print("3. Agregar Lector.")
            print("4. Prestar Libro.")
            print("5. Salir.")
            opc = int(input("Opción: "))
            if opc == 1:
                Clear.clear()
                l.addAuthor(Author(input("Ingrese el nombre: "), input("Ingrese la nacionalidad: "), input("Ingrese la fecha de nacimiento: ")))
                input("\nPresione una tecla para continuar...")
            elif opc == 2:
                Clear.clear()
                l.addBook(Author, Book(input("Ingrse el titulo: "), input("Ingrese el tipo: "), input("Ingrese la editorial: "), input("Ingrese el año: "), input("Ingrse el autor: ")))
                input("\nPresione una tecla para continuar...")
            elif opc == 3:
                Clear.clear()
                l.addReader(Reader(input("Ingre el nombre: ")))
                input("\nPresione una tecla para continuar...")
            elif opc == 4:
                Clear.clear()
                l.addBorrowed(Reader, Book)
                input("\nPresione una tecla para continuar...")
            elif opc == 5:
                Clear.clear()
                print("\n¿Está seguro que desea salir?\n1. Si.\n2. No.")
                close = int(input("> "))
                if close == 1:
                    Clear.clear()
                    break
                elif close == 2:
                    print("Regresando...")
                else:
                    print("\nOpción invalida, intente de nuevo.")
            else:
                print("\nOpción invalida, intente de nuevo.")

if __name__ == "__main__":
    Main.main()

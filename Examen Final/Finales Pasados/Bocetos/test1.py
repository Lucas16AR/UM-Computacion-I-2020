class Cola:
    def __init__(self):
        self.cajero = []
        print("Bienvenido al Banco")

    def nuevo_cliente(self):
        self.nombre_cliente = []
        cantidad_de_clientes = int(input("Ingrese la cantidad de clientes: "))
        for element in range(cantidad_de_clientes):
            nombre = str(input("Ingrese su nombre: "))
            self.nombre_cliente.insert(0, nombre)
        main()

    def turno(self):
        turno = int(input("""
.......................................................
. 1) Presione 1 para sacar turno                      .
.......................................................
"""))
        try:
            if turno == 1:
                self.cajero.append(self.nombre_cliente[-1])
                print("Ingrese al cajero 1: ", self.cajero)
                print(self.cajero, "se ha liberado")
                self.nombre_cliente.pop(-1)
                self.cajero.pop()
                print("El proximo cliente es: ", self.nombre_cliente[-1])
            else:
                print("No hay clientes para atender")
        except ValueError:
            print("Ingrese un valor valido")
        main()


def main():
    try:
        main = int(input("""
|-------------------------------------------|
| 1) Ingrese para ingresar sus datos        |      
| 2) Seleccione a que caja ir               |
| 3) Para salir                             |
|-------------------------------------------|
"""))
        if main == 1:
            Cola.nuevo_cliente()
        elif main == 2:
            Cola.turno()
        elif main == 3:
            exit()
        else:
            print("Ingrese una opcion correcta: ")
    except ValueError:
        print("Ingrese un valor valido: ")


Cola = Cola()
main()
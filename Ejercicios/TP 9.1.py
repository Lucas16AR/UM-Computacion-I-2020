class TorreDeControl:
    def __init__(self, aterrizar, despegar):
        self.aterrizar = aterrizar
        self.despegar = despegar
        print("Se ha iniciado la Torre de Control")

    def reconocimiento(self):
        element = int(input("""
Ingrese 1 para verificar los aviones que hay para aterrizar
Ingrese 2 para verificar los aviones que hay para despegar
"""))
        if element == 1:
            self.aterrizar = []
            aviones_aterrizar = int(input("Ingrese cuantos aviones hay para aterrizar: "))
            for i in range(aviones_aterrizar):
                aterrizar = input("Ingrese el avion que va a aterrizar: ")
                self.aterrizar.insert(0, aterrizar)
            main()
        if element == 2:
            self.despegar = []
            aviones_despegar = int(input("Ingrese cuantos aviones hay para despegar: "))
            for i in range(aviones_despegar):
                despegar = input("Ingrese el avion que va a despegar: ")
                self.despegar.insert(0, despegar)
            main()

    def accion(self):
        global inversa_aterrizaje, inversa_despege
        accion_a_realizar = int(input("""
Ingrese 1 para hacer despegar al avion
Ingrese 2 para hacer aterrizar al avion
"""))
        if accion_a_realizar == 1:
            inversa_despege = self.despegar
            inversa_despege.reverse()
            print("El avion que va a despegar es: ", inversa_despege[0])
            inversa_despege.pop()
            print("El avion ha despegado")
            main()
        elif accion_a_realizar == 2:
            inversa_aterrizaje = self.aterrizar
            inversa_aterrizaje.reverse()
            print("El avion que va a aterrizar es: ", inversa_aterrizaje[0])
            inversa_aterrizaje.pop()
            print("El avion ha aterrizado")
            main()

    def __str__(self):
        print("Los aviones que hay para aterrizar son: ", self.aterrizar)
        print("Los aviones que hay para despegar son: ", self.despegar)
        main()


def main():
    try:
        main = int(input(""""
|-----------------------------------------------------------------|
|****************BIENVENIDO A LA TORRE DE CONTROL*****************|
|1) Para verificar si hay algun avion por aterrizar o despegar    |
|2) Para hacer aterrizar o despegar un avion                      |
|3) Para ver el estado actual                                     |
|4) Salir                                                         | 
|-----------------------------------------------------------------|        
"""))
        if main == 1:
            TorreDeControl.reconocimiento()
        if main == 2:
            TorreDeControl.accion()
        if main == 3:
            TorreDeControl.__str__()
        if main == 4:
            print("Ha salido de la torre de control")
            exit()
        if main > 4:
            print("Ingrese un numero de opcion correcto")
    except ValueError:
        print("Ingrese una opcion valida")


TorreDeControl = TorreDeControl(aterrizar=0, despegar=0)
main()
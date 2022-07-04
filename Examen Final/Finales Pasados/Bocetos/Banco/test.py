class Banco:
    def __init__(self, espera, atencion, atendido):
        self.espera = espera
        self.atencion = atencion
        self.atendido = atendido
        print("Se ha iniciado el Banco UM")

    def reconocimiento(self):
        element = int(input("""
Ingrese 1 para agregar a la fila para espera
Ingrese 2 para agregar a la fila para atencion
Ingrese 3 para anotar los atendidos
"""))
        if element == 1:
            self.espera = []
            cliente_espera = int(input("Ingrese cuantas personas hay en espera: "))
            for i in range(cliente_espera):
                espera = input("Ingrese el ID del cliente que va a esperar: ")
                self.espera.insert(0, espera)
            main()
        if element == 2:
            self.atencion = []
            cliente_atencion = int(input("Ingrese cuantas personas estan atendidas: "))
            for i in range(cliente_atencion):
                atencion = input("Ingrese el ID que va a ser atendida: ")
                self.atencion.insert(0, atencion)
            main()
        if element == 3:
            self.atendido = []
            cliente_atendido = int(input("Ingrese cuantas personas han sido atendidas: "))
            for i in range(cliente_atendido):
               atendido = input("Ingrese el ID de quien fue atendido: ")
               self.atendido.insert(0, atendido)
            main()    


    def accion(self):
        global inversa_espera, inversa_atencion, inversa_atendido
        accion_a_realizar = int(input("""
Ingrese 1 para hacer atencion al cliente
Ingrese 2 para hacer esperar al cliete
"""))
        if accion_a_realizar == 1:
            inversa_atencion = self.atencion
            inversa_atencion.reverse()
            print("El cliente que va a ser atendido es: ", inversa_atencion[0])
            inversa_atencion.pop()
            print("El cliente ha sido atendido")
            main()
        elif accion_a_realizar == 2:
            inversa_espera = self.espera
            inversa_espera.reverse()
            print("El cliente que va a esperar es: ", inversa_espera[0])
            inversa_espera.pop()
            print("El cliente esta siendo atendido")
            main()
        elif accion_a_realizar == 3:
            inversa_atendido = self.atendido
            inversa_atendido.reverse()
            print("El cliente que fue atendido fue: ", inversa_atendido[0])
            inversa_atendido.pop()
            print("El cliente fue atendido")
            main()


    def __str__(self):
        print("Los clientes que hay para atender son: ", self.espera)
        print("Los clientes que hay en atencion son: ", self.atencion)
        print("Los clientes que han sido atendidos son : ", self.atendido)
        main()


def main():
    try:
        main = int(input(""""
|-----------------------------------------------------------------|
|****************BIENVENIDO Al BANCO******************************|
|1) Para verificar si hay alguien por espera o atencion           |      
|2) Para hacer espera o atencion                                  |
|3) Para ver el estado actual                                     |
|4) Salir                                                         | 
|-----------------------------------------------------------------|        
"""))
        if main == 1:
            Banco.reconocimiento()
        if main == 2:
            Banco.accion()
        if main == 3:
            Banco.__str__()
        if main == 4:
            print("Ha salido....")
            exit()
        if main > 4:
            print("Ingrese un numero de opcion correcto")
    except ValueError:
        print("Ingrese una opcion valida")


Banco = Banco(espera = 0, atencion = 0, atendido = 0)
main()
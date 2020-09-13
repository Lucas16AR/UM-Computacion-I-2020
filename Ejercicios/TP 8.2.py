mates_servidos = int(input("Cuantas veces quiere cebar antes de que se lave: "))

class Mate():
    
    def __init__(self, cantdecebadas, estadodemate,):
        self.cantdecebadas = cantdecebadas
        self.estadodemate = estadodemate
        print("Esta listo el mate")
    
    def cambiar_yerba(self):
        self.cantdecebadas = cantdecebadas
        print("Se cambio la yerba")
        Accion()

    def cebar(self):
            if not self.estadodemate:
                self.estadodemate = True
                print("Se lleno ya")
                Accion()
            else:
                print("Te quemaste")
                Accion()

    def tomar(self):
        if self.estadodemate:
            self.estadodemate = False
            print("¿Gusto o no gusto el mate?")
            if self.cantdecebadas != 0:
                self.cantdecebadas -= 1
                print("Cantidad de cebadas restantes antes de lavarse: {}".format(self.cantdecebadas))
                Accion()
            else:
                print("Se lavó el mate")
                Accion()
        else:   
            print("El mate no tiene agua, servir de vuelta")
            Accion()

def Accion():
    try:
        accion = int(input("""
[1] = Cebar Mate
[2] = Tomar Mate
[3] = Cambiar Yerba
>>: """))
        if accion == 1:
            mate.cebar()
        if accion == 2:
            mate.tomar()
        if accion == 3:
            mate.cambiar_yerba()
        else:
            print("Valor ingresado no es el correcto")
            Accion()
    except ValueError:
        print("Valor ingresado no es el correcto")
        accion()

cantdecebadas = mates_servidos
mate = Mate(cantdecebadas, False)
Accion()
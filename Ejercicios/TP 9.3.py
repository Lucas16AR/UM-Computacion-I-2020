from os import system
class Carta:
    
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        #print('Se ha creado una carta')
    
    def __str__(self):
        return 'Carta de {} con un valor de {}'.format(self.palo, self.valor)

class PilaDeCartas:
      
    cartas = []

    def __init__(self, cartas=[]):
        self.cartas = cartas

    def agregarCartaALaPila(self, c):
        if c.palo != self.cartas[-1].palo and c.valor < self.cartas[-1].valor:
            self.cartas.append(c)
            print("\033[;36m")
            print('La carta: {} ha sido agregada a la pila'.format(c))

        else:
            print("\033[;36m")
            print('La carta: {} no ha sido agregada a la pila porque no cumple con las condiciones'.format(c))


    def mostrar(self):
        for c in self.cartas:
            print(c) 

def agregar_Carta():
    system('cls')
    ObjetosCreados = False
    try:
        largo = int(input("""¿Cuantas cartas desea agregar a su pila?
>>>: """))
    except ValueError:
        agregar_Carta()

    for i in range(largo):
        print("\033[;37m")
        try:
            paloOpcion = int(input("""
Eliga el palo de la carta a añadir a la pila de cartas
[1]Oro
[2]Espada
[3]Palo
[4]Copa    
>>>: """))
            palo = ''
            if paloOpcion == 1:
                palo = 'Oro'
            elif paloOpcion == 2:
                palo = 'Espada'
            elif paloOpcion == 3:
                palo = 'Palo'
            elif paloOpcion == 4:
                palo = 'Copa'
            else:
                print('Por favor ingrese una opcion valida')
                agregar_Carta()
        except ValueError:
            agregar_Carta() 

        try:
            valor = 0
            valorOpcion = int(input("""
Por favor ingrese un valor del 1 al 12    
>>>: """))
            if valorOpcion > 0 and valorOpcion < 13:
                valor = valorOpcion
            else:
                print('Por favor ingrese un valor correctamente')
                agregar_Carta


            if not ObjetosCreados:
                c = Carta(palo, valor)
                p = PilaDeCartas([c])
                ObjetosCreados = True
                print("\033[;36m")
                print('Primera carta agregada correctamente')
                

            else:
                p.agregarCartaALaPila(Carta(palo, valor))
        except ValueError:
            agregar_Carta()

        
    system('cls')
    print("\033[;36m")
    print('Todas las cartas que fueron agregadas a la pila:')
    p.mostrar()

agregar_Carta()
class Orco():
    ataque1 = False
    def __init__(self, nombre, edad, vida, daño, rango_ataque, coste_unidad):
        self.nombre = nombre
        self.edad = edad
        self.vida = vida
        self.daño = daño
        self.rango_ataque = rango_ataque
        self.coste_unidad = coste_unidad
    
    def ataque(self):
        self.ataque1 = True
        print(self.nombre, "Esta atacando")

    def presentarse(self):
        print("\nnombre: ", self.nombre, "\nedad:", self.edad, "\nvida", self.vida, "\ndaño", self.daño, "\nrango_ataque", self.rango_ataque, "\ncoste_unidad", self.coste_unidad)

class OrcoGuerrero(Orco):
    def __init__(self, nombre, edad, vida):
        self.nombre = nombre
        self.edad = edad
        self.vida = vida
        self.daño = 12
        self.rango_ataque = 2
        self.coste_unidad = 250

class OrcoLancero(Orco):
    def __init__(self, nombre, edad, vida):
        self.nombre = nombre
        self.edad = edad
        self.vida = vida
        self.daño = 8
        self.rango_ataque = 4
        self.coste_unidad = 150
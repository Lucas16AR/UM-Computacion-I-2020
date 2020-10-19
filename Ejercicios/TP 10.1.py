class Humano():
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
        print(self.nombre, "esta atacando")

    def presentarse(self):
        print("\nnombre: ", self.nombre, "\nedad:", self.edad, "\nvida: ", self.vida, "\ndaño", self.daño, "\nrango_ataque", self.rango_ataque, "\ncoste_unidad", self.coste_unidad)
    
class HumanoGuerrero(Humano):
    def __init__(self, nombre, edad, vida):
        self.nombre = nombre
        self.edad = edad
        self.vida = vida
        self.daño = 9
        self.rango_ataque = 2
        self.coste_unidad = 150

class HumanoArquero(Humano):
    def __init__(self, nombre, edad, vida):
        self.nombre = nombre
        self.edad = edad
        self.vida = vida
        self.daño = 6
        self.rango_ataque = 8
        self.coste_unidad = 100
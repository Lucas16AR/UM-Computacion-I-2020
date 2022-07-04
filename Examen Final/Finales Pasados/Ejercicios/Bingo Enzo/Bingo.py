import Carton from *
import Programa from *
import random

lista_extraidas = []
lista_bombo = []
lista_comprador = []


class Bingo:
    def __init__(self, bolas, carton, ultima_b):
        self.bolas = bolas
        self.carton = carton
        self.ultima_b = ultima_b

    def contador(self):
        cantidad = int(input("Con cuantas bolas desea jugar"))
        return cantidad
        for i in range(0, cantidad):
            lista_bombo.append(i)
            i = i + 1

    def bola_ramdom(self):
        bola_aleatoria = random.randint(cantidad)
        return bola_aleatoria
        lista_extraidas.append(bola_aleatoria)
        lista_bombo.pop(bola_aleatoria)
        lista_comprador.append(bola_aleatoria)

    def comparador(self):
        print(max(lista_comprador))

    def ultima_bola(self):
        ultima_bola = bola_aleatoria

    def mostrar (self):
        print(lista_extraidas)

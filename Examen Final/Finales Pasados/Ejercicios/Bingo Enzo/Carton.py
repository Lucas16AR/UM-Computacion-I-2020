from Bingo import *
from Programa import *


lista_carton = []


class Carton:
    def __init__(self, id, numeros, tamaño):
        self.id = id
        self.numeros = numeros
        self.tamaño = tamaño

    def armar_carton(self, id, numeros, tamaño):
        n_carton = print(int(input("Con cuantos numeros desea jugar en el carton")))
        for i in range(n_carton):
            lista_carton.append(random.randint(cantidad))

    def bingo(self):
        if lista_carton in lista_extraidas:
            print("Tenemos un ganador")
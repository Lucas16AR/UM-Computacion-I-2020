from io import *

file = open("ej4.txt", "w")
file.write("Python es un lenguaje de programación interpretado")
file.write("\nSe trata de un lenguaje de programación multiparadigma")
file.write("\nSoporta orientación a objetos, programación imperativa")
file.write("\nEn menor medida, programación funcional")

file.close()

file = open("ej4.txt", "r")
lista = file.readlines()
print(lista)
file.close()
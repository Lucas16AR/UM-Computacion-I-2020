from io import *

file = open("ej3.txt", "w")
texto = str(input("Ingrese el texto para agregar: "))
file.write(texto)
file.close()

file = open("ej3.txt", "r")
print(file.read())
file.close()
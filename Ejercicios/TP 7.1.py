from io import *

file = open("ej1.txt", "w")
file.write ("Primer Archivo de Manejo de Archivos")
file.close()

file = open("ej1.txt", "r")
print(file.read())
file.close()
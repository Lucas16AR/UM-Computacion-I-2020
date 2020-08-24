from io import *

file = open("ej2.txt", "w")
file.write("Segundo Archivo de Manejo de Archivo")
file.close()

file = open("ej2.txt", "a")
file.write("\nEl Ejercicio de hoy trata sobre el Manejo de Archivos")
file.close()

file = open("ej2.txt", "r")
print(file.read())
file.close()
from io import *

file = open("ej5.1.txt", "w")
file.write("Los programadores de Python viven su dia a dia como cualquier otro programador")
file.close()

file = open("ej5.1.txt", "r")
lista = file.readlines()
file.close()

textcopy = open("ej5.2.txt", "w")
for i in lista:
    textcopy.write(i)
textcopy.close()
from io import *

file = open('ej6.txt', 'r')

num_lines = int(input('Ingrese la cantidad de lineas que desea leer: '))
print('\n')

lines = file.readlines()

file.close()

for i in range(num_lines):
    print(lines[i])
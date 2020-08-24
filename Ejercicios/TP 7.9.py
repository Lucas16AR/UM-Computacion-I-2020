from io import *
import re

expre = str(input('Ingrese una expresion para buscar en el fichero: '))

file = open('ej9.txt', 'r')
text = file.read()

file.close()
try:
    x = re.search(expre, text)
    position = x.span()
    print('El fragmento de texto buscando en el fichero se encuentra en la posicion: {}'.format(position))
except AttributeError:
    print('Ese fragmento no se encuentra en ninguna parte del texto')
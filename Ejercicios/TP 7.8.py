from io import *

file = open('ej8.txt', 'r')
lines = file.readlines()
file.close()

num_lines = 0
num_words = 0
num_chars = 0

for line in lines:
    num_lines += 1

    if line.startswith != '\n':
        words_in_line = line.split(None)
        num_words += len(words_in_line)

file = open('ej8.txt', 'r')
text = file.read()
chars = list(text)

for char in chars:
    if char != ' ':
        num_chars += 1

print("""
La cantidad de lineas que contiene el texto es: {}
La cantidad de palabras que contiene el texto es: {}
La cantidad de caracteres que contiene el texto es: {}
""".format(num_lines, num_words, num_chars))
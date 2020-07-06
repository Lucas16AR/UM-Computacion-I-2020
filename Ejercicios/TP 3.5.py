word = str(input('Ingrese una palabra: '))

letters_A = word.count('a')
letters_E = word.count('e')
letters_I = word.count('i')
letters_O = word.count('o')
letters_U = word.count('u')

print('La cantidad de veces que la letra "a" aparece en', word, 'es:', letters_A)
print('La cantidad de veces que la letra "e" aparece en', word, 'es:', letters_E)
print('La cantidad de veces que la letra "i" aparece en', word, 'es:', letters_I)
print('La cantidad de veces que la letra "o" aparece en', word, 'es:', letters_O)
print('La cantidad de veces que la letra "u" aparece en', word, 'es:', letters_U)
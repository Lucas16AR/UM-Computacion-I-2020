class Ciudad:
    def __init__(self, nombre, es_capital, cantidad_de_habitantes, lengua, zona_horaria):
        self.__nombre = nombre
        self.__es_capital = es_capital
        self.__cantidad_de_habitantes = cantidad_de_habitantes
        self.__lengua = lengua
        self.__zona_horaria = zona_horaria

    def get_nombre(self):
        return self.__nombre

    def get_es_capital(self):
        return self.__es_capital

    def get_cantidad_de_habitantes(self):
        return self.__cantidad_de_habitantes

    def get_lengua(self):
        return self.__lengua

    def get_zona_horaria(self):
        return self.__zona_horaria

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_es_capital(self, es_capital):
        self.__es_capital = es_capital

    def set_cantidad_de_habitantes(self, cantidad_de_habitantes):
        self.__cantidad_de_habitantes = cantidad_de_habitantes

    def set_lengua(self, lengua):
        self.__lengua = lengua

    def set_zona_horaria(self, zona_horaria):
        self.__zona_horaria = zona_horaria

    def to_str(self):
        return "El nombre de la ciudad es: ", self.__nombre, ",la capital es: ", self.__es_capital, \
               "la catidad de habitantes es de: ", self.__cantidad_de_habitantes, "el idioma que se habla es: ", \
               self.__lengua, "y la zona horaria es: ", self.__zona_horaria


ciudad = Ciudad("Mendoza", "Mendoza", 2086000, "Español", "GMT")
print(ciudad.to_str())

lista_pares = [e for e in range(1, 43) if e % 2 == 0]
print(lista_pares)
"""
import re


def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[" \
                        r"\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(" \
                        r"?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[" \
                        r"0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[" \
                        r"0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[" \
                        r"\x01-\x09\x0b\x0c\x0e-\x7f])+)\]) "
    return re.match(expresion_regular, correo) is not None


correos = ["hola@", "contacto@parzibyte.me", "staff@hotmail.com",
           "juan.perez@sitio.com", "maggie@outlook.com", "parzibyte@gmail.com", "asd",
           "luis@gmail@hotmail.com"]

for correo in correos:
    print("Probando si '{}' es válido...{}".format(correo, es_correo_valido(correo)))
"""
'''
letra = input("Ingrese una letra: ")
letra_d = 0
while letra != 's':
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
    for i in range(len(frase)):
        if frase[i] == 'd':
            letra_d = letra_d + 1
    print("Las palabras que empiezan con 'd' son:", letra_d)
if letra == 's':
    exit()
'''
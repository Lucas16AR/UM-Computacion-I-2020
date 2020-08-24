import io

listaCampo = []
archivo = open("ej7.txt", "r")
delimitador = input("Ingrese un delimitador a usar: ")
listaLineasArchivo = archivo.readlines()
for number in range(len(listaLineasArchivo)):
    name, score, time = listaLineasArchivo[number].split("-")
    listaCampo.append(name)
print(delimitador.join(listaCampo))
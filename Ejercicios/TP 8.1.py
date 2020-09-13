limiteSuperior = 10
limiteInferior = 0
def calculateFib(tamaño):
    try:
        assert (tamaño > limiteInferior)
        assert (tamaño < limiteInferior)
    except AssertionError:
        print("El valor debe estar entre 0 y 10")
    salida = []
    numero1, numero2 = 0, 1
    for x in range(tamaño):
        salida.append(numero2)
        numero1, numero2 = numero2, numero1+numero2
    return salida

def main():
    try:
        entrada = input("Ingrese el tamaño a calcular: ")
        n = int(entrada)
        print(calculateFib(n))
    except ValueError:
        print("Ingrese un numero entre 0 y 10 que sea entero")
        
main()
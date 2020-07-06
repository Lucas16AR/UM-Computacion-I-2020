print("Calculadora de 4 funciones")

def calculator(operation):
    if operation == "1":
        num1 = int(input("Ingrese un número para sumar: "))
        num2 = int(input("Ingrese otro número para sumar: "))
        result = num1 + num2
    if operation == "2":
        num1 = int(input("Ingrese un número para restar: "))
        num2 = int(input("Ingrese otro número para restar: "))
        result = num1 - num2
    if operation == "3":
        num1 = int(input("Ingrese un número para multiplicar: "))
        num2 = int(input("Ingrese un número para multiplicar: "))
        result = num1 * num2
    if operation == "4":
        num1 = int(input("Ingrese un número para dividir: "))
        num2 = int(input("Ingrese un número para dividir: "))
        result = num1 / num2
    print("Resultado es", result)
    
option = str(input("Para sumar ingrese 1, para restar ingrese 2, para multiplicar ingrese 3, para dividir ingrese 4: "))
calculator(option)
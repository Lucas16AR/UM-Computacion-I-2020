#Ejercicio1
print("HOLA MUNDO")

#Ejercicio2
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
print("Resultado es", num1+num2)

#Ejercicio3
product = 200
IVA = 1.21
valorfinal= (product * IVA)
print (valorfinal)

#Ejercicio4
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
lista = []
lista.append(num1)
lista.append(num2)
print("El nùmero mayor es", max(lista))

#Ejercicio5 y Ejercicio6
var = int(input("Ingrese un nùmero: "))
if var > 0 and var <= 10:
    print("El nùmero", var, "esta entre 0 y 10")
if var > 11 and var <= 20:
    print("El nùmero", var, "esta entre 11 y 20")
if var > 21 and var <= 30:
    print("El nùmero", var, "esta entre 21 y 30")
if var > 31 and var <=999999999999999999999999999999999999999:
    print("El nùmero", var, "no se encuentra en ninguno de esos 3 rangos")

#Ejercicio7
cons = 1
while 1 != 0:
    print(cons)
    cons = cons + 1
    if cons == 51:
        break

#Ejercicio8
for N in range (50+1):
    print(N)

#Ejercicio9
print(len("HOLA MUNDO"))

#Ejercicio10
for C in range(100+1):
    if (-1)**C == 1:
        print(C, 'es par')
    else:
        print(C, 'es impar')
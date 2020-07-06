list_ = []
for i in range (5):
    add = int(input("Ingrese un precio para agregar a la lista: "))
    list_.append(add)
print('El precio mayor de la lista es:', max(list_))
print('El precio menor de la lista es:', min(list_))
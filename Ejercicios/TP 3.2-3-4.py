#ejercicio2
list_ = []
add_1 = int(input("Ingrese las cantidad de materias del primer semestre de Ingenieria en Informática: "))
for i in range(add_1):
    add = str(input("Ingrese una materia: "))
    list_.append(add)
print(list_)
for i in range(len(list_)):
    print("Yo estoy estudiando: ", list_[i])

#ejercicio3
notes = []
for i in range(len(list_)):
    add = int(input(f"Ingrese la nota que se ha sacado en {list_[i]}: "))
    notes.append(add)

#ejercicio4
for i in range(len(list_)):
    print(f"En {list_[i]} te has sacado un {notes[i]}")
list_classes = []
notes = []

add_1 = int(input("Ingrese cuantas materias cursó en segundo año: "))
for i in range(add_1):
    add_2 = str(input('Ingrese materia: '));
    list_classes.append(add_2);
    add_3 = int(input(f'Ingrese la nota que se ha sacado en {list_classes[i]} : '))
    notes.append(add_3)
for i in range(add_1):
    if notes[i] >= 6:
        list_classes[i] = 0
list_classes = list(set(list_classes))
list_classes.remove(0)
print('Las materias que tienes que recursar son:', list_classes)
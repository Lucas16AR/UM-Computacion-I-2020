import universidad
from alumno import Alumno
import carrera
from inscripcion import Inscripcion
import constante_final


def main():
    menu = constante_final.MAIN
    if menu == 1:
        inscripcion = Inscripcion('Delfina Quinteros', 'computacion', '4/3/12')
        print(inscripcion)
    elif menu == 2:
        exit()
    else:
        print("Ingrese una opcion valida")


main()

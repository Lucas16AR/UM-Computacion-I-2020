class ColaDePacientes:
    def __init__(self):
        self.traumatologo = []
        self.clinico = []
        self.oftalmologo = []
        self.nombre_paciente = []
        print("Bienvenido a la clinica")

    def nuevo_paciente(self):
        self.nombre_paciente = []
        cantidad_de_pacientes = int(input("Ingrese la cantidad de clientes: "))
        for element in range(cantidad_de_pacientes):
            nombre = str(input("Ingrese su nombre: "))
            self.nombre_paciente.insert(0, nombre)
        main()

    def turno(self):
        doctor = int(input("""
.......................................................
. 1) Presione 1 si tiene turno con el traumatologo    .
. 2) Presione 2 si tiene turno con el medico clinico  .
. 3) Presione 3 si tiene turno con el oftalmologo     .
.......................................................
"""))
        try:
            if doctor == 1:
                self.traumatologo.append(self.nombre_paciente[-1])
                print("Ingrese al consultorio del traumatologo: ", self.traumatologo)
                print(self.traumatologo, "se ha liberado")
                self.nombre_paciente.pop(-1)
                self.traumatologo.pop()
                print("El proximo paciente es: ", self.nombre_paciente[-1])
            elif doctor == 2:
                self.clinico.append(self.nombre_paciente[-1])
                print("Ingrese al consultorio del clinico: ", self.clinico)
                print(self.clinico, "se ha liberado")
                self.nombre_paciente.pop(-1)
                self.clinico.pop()
                print("El proximo paciente es: ", self.nombre_paciente[-1])
            elif doctor == 3:
                self.oftalmologo.append(self.nombre_paciente[-1])
                print("Ingrese al consultorio del oftalmologo: ", self.oftalmologo)
                print(self.oftalmologo, "se ha liberado")
                self.nombre_paciente.pop(-1)
                self.oftalmologo.pop()
                print("El proximo paciente es: ", self.nombre_paciente[-1])
            else:
                print("No hay clientes para atender")
        except ValueError:
            print("Ingrese un valor valido")
        main()


def main():
    try:
        main = int(input("""
|-------------------------------------------|
| 1) Ingrese para ingresar sus datos        |      
| 2) Seleccione a que medico tiene turno    |
| 3) Para salir                             |
|-------------------------------------------|
"""))
        if main == 1:
            ColaDePacientes.nuevo_paciente()
        elif main == 2:
            ColaDePacientes.turno()
        elif main == 3:
            exit()
        else:
            print("Ingrese una opcion correcta: ")
    except ValueError:
        print("Ingrese un valor valido: ")


ColaDePacientes = ColaDePacientes()
main()
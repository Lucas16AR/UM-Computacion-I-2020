class Alumno:
    def __init__(self, nombre, apellido, dni, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail

    def __str__(self):
        return "La alumna: " + "" + self.nombre + " " + self.apellido + " " + ", dni: " + self.dni + ", mail: " + self.mail


alumno = Alumno('Delfina', 'Quinteros', '42974437', 'de.quinteros@gmail.com')
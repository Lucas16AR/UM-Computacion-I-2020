class Inscripcion:
    def __init__(self, alumno, materia, fecha_inscripcion):
        self.alumno = alumno
        self.materia = materia
        self.fecha_inscripcion = fecha_inscripcion

    def __str__(self):
        return "La alumna: " + self.alumno + ", se va a inscribir en: " + self.materia + ", en la fecha: " + self.fecha_inscripcion


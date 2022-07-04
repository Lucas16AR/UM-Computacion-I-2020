class Libro():

    def __init__(self, name, tipo, editorial, año, autor):
        self.name = name
        self.tipo = tipo
        self.editorial = editorial
        self.año = año
        self.autor = autor


    def __repr__(self):
        return f"Nombre: {self.name} ----- Tipo: {self.tipo} ----- Editorial: {self.editorial} ----- Año: {self.año} ----- Autor: {self.autor}"
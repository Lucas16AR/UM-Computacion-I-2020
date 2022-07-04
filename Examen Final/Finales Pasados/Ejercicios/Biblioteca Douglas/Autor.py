class Author:
    def __init__(self, name, nationality, date):
        self.name = name
        self.nationality = nationality
        self.date = date

    def __repr__(self) -> str:
        return f"Nombre: {self.name}, nacionalidad: {self.nationality}, año de nacimiento{self.date}"
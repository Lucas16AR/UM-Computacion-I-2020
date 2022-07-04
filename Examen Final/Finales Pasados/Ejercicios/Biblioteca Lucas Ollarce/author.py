class Author():
    def __init__(self, name, nationality, birthdate):
        self.name = name
        self.nationality = nationality
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.name}, {self.nationality}, {self.birthdate}"

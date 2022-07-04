class Book():
    def __init__(self, title, type, editorial, year, author):
        self.title = title
        self.type = type
        self.editorial = editorial
        self.year = year
        self.author = author

    def __str__(self):
        return f"{self.title}, {self.type}, {self.editorial}, {self.year}, {self.author}"

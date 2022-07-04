from sqlalchemy import desc


class Book:
    
    def __init__(self, title, description, editorial, year, author):
        self.title = title
        self.description = description
        self.editorial = editorial
        self.year = year
        self.author = author

    def __repr__(self):
        return f"Libro: {self.title}, {self.description}, {self.editorial}, {self.year}, {self.author}"
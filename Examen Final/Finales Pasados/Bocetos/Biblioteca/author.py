class Author:

    def __init__(self, name, nationality, date):
        self.name = name
        self.nationality = nationality
        self.date = date

    def __repr__(self):
        return f"Author: {self.name}, {self.nationality}, {self.date}"
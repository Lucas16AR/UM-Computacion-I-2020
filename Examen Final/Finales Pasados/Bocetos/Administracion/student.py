class Student:

    def __init__(self, name, surname, id, email):
        self.name = name
        self.surname = surname
        self.id = id
        self.email = email

    def __repr__(self):
        return f'Student: {self.name} {self.surname} {self.id} {self.email}'
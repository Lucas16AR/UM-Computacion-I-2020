class Client:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Cliente: {self.name}, {self.surname}"
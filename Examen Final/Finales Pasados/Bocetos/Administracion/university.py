class University:

    def __init__(self, name, address, web):
        self.name = name
        self.address = address
        self.web = web

    def __repr__(self):
        return f'University: {self.name}, {self.address}, {self.web}'
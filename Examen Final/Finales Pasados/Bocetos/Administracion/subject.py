class Subject:

    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students: list = []

        def __repr__(self):
            return f'Subject: {self.name}, {self.code}, {self.students}'
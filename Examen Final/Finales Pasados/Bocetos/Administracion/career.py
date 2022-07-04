import re
class Career:

    def __init__(self, name, description, university):
        self.name = name
        self.description = description
        self.subjects: list = []
        self.university = university

    def __repr__(self):
        return f"Career: {self.name}, {self.description}, {self.subjects}, {self.university}"
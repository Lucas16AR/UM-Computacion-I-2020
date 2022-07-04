
class Carton:
    def __init__(self, Id, numbers, leng):
        self.Id = Id
        self.numbers = numbers
        self.leng = leng

    def __str__(self):
        return """
ID CARTON:  {}
NUMEROS:    {}
TAMAÑO:     {}   
""".format(self.Id, self.numbers, self.leng)

    def isBingo(self):
        pass
class Robot:

    #atributos
    def __init__(self):
        self.name = ""
        self.height = ""
        self.proccessador = ""
        self.date = ""

    #estado
    isOff = False
    isOn = True
    isDamaged = False

    def works(self):
        self.isOn = True

    def stop(self):
        self.isOn = False

    def showStatus(self):
        if(self.isOn):
            return "Robot Funciona Correctamente"
        else:
            return "Robot No Funciona Correctamente"

Machine_1 = Robot()

print(Machine_1.works())
print(Machine_1.showStatus())
print((Machine_1.stop()))
print(Machine_1.showStatus())
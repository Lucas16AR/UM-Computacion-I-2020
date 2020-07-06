class Keyboards():

    def __init__(self, keyboards, distribution):
        self.keyboards = keyboards
        self.distribution = distribution


class Flexible(Keyboards):
    pass


class Membrane(Keyboards):
    pass


class Mechanic(Keyboards):

    def __init__(self, keyboards, distribution, switches):
        self.keyboards = keyboards
        self.distribution = distribution
        self.switches = switches

    def saltar(self):
        pass


hyperX_alloy_fps = Mechanic("Mecanico", "QWERTY", "Cherry RED")
redragon_dyauz_k509 = Membrane("Membrana", "QWERTY")

print(hyperX_alloy_fps.switches)
print(redragon_dyauz_k509.distribution)
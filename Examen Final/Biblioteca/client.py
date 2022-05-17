class Client():

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __repr__(self):
        return f'Client: {self.name} {self.age} {self.country}'

'''
client1 = Client("Lucas Galdame", 21, "Argentina")
client2 = Client("Gaston Fenske", 23, "Argentina")
client3 = Client("Bruno Romero", 22, "Argentina")

print(client1)
'''
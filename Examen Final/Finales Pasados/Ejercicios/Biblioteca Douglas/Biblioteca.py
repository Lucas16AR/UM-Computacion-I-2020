class Biblioteca:
    listaClientes = []
    listaLibros = []
    asignaciones = {}

    def Assign(self, cliente, libro):
        self.asignaciones[cliente] = libro
        print(self.asignaciones)

    def AddClient(self, cliente):
        self.listaClientes.append(cliente)

    def AddBook(self, libro):
        self.listaLibros.append(libro)

    def ShowClients(self):
        for cliente in self.listaClientes:
            print(cliente.View())
            
    def ShowBooks(self):
        for book in self.listaLibros:
            print(book.View())

    def SearchClient(self, name):
        for cliente in self.listaClientes:
            if cliente.name == name:
                return cliente

    def SearchBook(self, name):
        for libro in self.listaLibros:
            if libro.name == name:
                return libro
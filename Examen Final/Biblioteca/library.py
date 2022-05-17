class Library:
    
    list_clients = []
    list_books = []
    assigned_books = []

    def AddClient(self, client):
        self.list_clients.append(client)

    def Assign(self, book):
        self.assigned_books[book] = book
        print(self.assigned_books)

    def AddBook(self, book):
        self.list_books.append(book)

    def SearchClient(self, name):
        for client in self.list_clients:
            if client.name == name:
                return client

    def SearchBook(self, name):
        for book in self.list_books:
            if book.name == name:
                return book

    def ShowClients(self):
        for client in self.list_clients:
            print(client.View())
    
    def ShowBooks(self):
        for book in self.list_books:
            print(book.View())

    def AddBorrowed(self, reader, book): 
        self.borrowed[reader] = book

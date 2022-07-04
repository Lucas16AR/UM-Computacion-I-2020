class Function:
    
    books = []

    authors = ["Paulo Coehlo", "Gabriel Garcia Marquez"]

    clients = []

    borrowed = ["11 Minutos"]

#-----------------------------------------------------------------

    def addBook(self, book):
        self.books.append(book)

    def addAuthor(self, author):
        self.authors.append(author)

    def addClient(self, client):
        self.clients.append(client)

    def addBookReader(self, reader, book):
        self.borrowed[reader] = book

#----------------------------------------------------------------

    def viewBook(self):
        for books in self.books:
            print(books)

    def viewAuthor(self, author):
        for author in self.authors:
            print(author.name)

    def viewClient(self):
        for client in self.clients:
            print(client)

    def viewBorrowed(self):
        for borrowed in self.borrowed:
            print(borrowed)
        
    #print(client)
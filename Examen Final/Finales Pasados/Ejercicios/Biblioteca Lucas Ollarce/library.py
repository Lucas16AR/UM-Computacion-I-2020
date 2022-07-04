class Library():
    books = {}
    authors = []
    readers = []
    borrowed = {}

    def addAuthor(self, author):
        self.author.append(author)

    def addBook(self, author, book):
        self.books[author] = book

    def addReader(self, reader):
        self.readers.append(reader)

    def addBorrowed(self, reader, book): 
            self.borrowed[reader] = book

    def viewBook(self):
        for book in self.books:
            print(book)

    def viewAuthor(self):
        for author in self.authors:
            print(author)

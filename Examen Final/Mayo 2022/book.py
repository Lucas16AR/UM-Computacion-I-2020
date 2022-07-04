class Book():

    def __init__(self, name, author, isb):
        self.name = name
        self.author = author
        self.isb = isb

    def __repr__(self):
        return f'Book: {self.name} {self.author} {self.isb}'

'''
book1 = Book("yo y el", "carlos ruiz", 21)
book2 = Book("before you", "ruth barrios", 15)
book3 = Book("after you", "ruth barrios", 19)

print(book1)
'''
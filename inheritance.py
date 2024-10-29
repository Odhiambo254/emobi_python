#creating a parent

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

#creating child class

class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed :
            self.is_borrowed = False
            print(f'{self.title} has been borrowed by {self.author}.')
        else:
            print(f'{self.title} is already borrowed.')

book=FictionBook(title="inherited", author="andrew", genre="inherited")
book.borrow()
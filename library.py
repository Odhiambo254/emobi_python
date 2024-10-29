# managing a library system
# parent class
class Book:
    def __init__(self,tittle,author):
        self.tittle=tittle
        self.author=author
    def display_info(self):
        return f"The Tittle {self.tittle},Author {self.author}"
# child class/ derived class

class LibraryBook(Book):
    def __init__(self,tittle,author,isbn,copies_available):
        super().__init__(tittle,author)
        self.isbn=isbn
        self.copies_available=copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -=1
            return f"{self.tittle} borrowed. Copies left: {self.copies_available}"
        else:
            return f"No of copies  {self.tittle} unavailable"
    def return_book(self):
        self.copies_available +=1

        return f"{self.tittle} returned. Copies left: {self.copies_available}"
    # usage example
book1=LibraryBook("Inheritance","Adrian",123456-986,20)

print(book1.display_info())

print(book1.borrow_book())

print(book1.return_book())
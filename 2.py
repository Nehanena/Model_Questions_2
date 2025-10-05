# . Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book, library):
        try:
            library.lend_book(book, self)
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        except Exception as e:
            print(f"Error: {e}")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            library.receive_book(book)
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} doesn't have '{book.title}'")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, book, member):
        if book in self.books and not book.is_borrowed:
            book.is_borrowed = True
        else:
            raise Exception(f"'{book.title}' is not available")

    def receive_book(self, book):
        book.is_borrowed = False

    def show_available_books(self):
        print("\nAvailable books:")
        for book in self.books:
            if not book.is_borrowed:
                print(f"- {book.title} by {book.author}")
        print()

if __name__ == "__main__":
    library = Library()
    book1 = Book("1984", "George Orwell")
    book2 = Book("The Alchemist", "Paulo Coelho")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    book4 = Book("Geetanjali", "Rabindra Nath Tagore")
    book5 = Book("Arthashastra", "Kautilya")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    Nandhana = Member("Alice")
    Devika = Member("Bob")
    library.show_available_books()

    Nandhana.borrow_book(book1, library)
    Devika.borrow_book(book3, library)  
    Nandhana.return_book(book4, library)
    Devika.borrow_book(book2, library)
    Nandhana.borrow_book(book5,library)

    library.show_available_books()

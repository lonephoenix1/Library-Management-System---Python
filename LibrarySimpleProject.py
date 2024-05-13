class Book:
    def __init__(self, isbn, title, author, year_of_publication):
        # Initialize a Book instance with attributes such as ISBN, title, author, year of publication, and status.
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.status = 'available'  # Initially set the status of the book as 'available'.

    def borrow_book(self):
        # Method to borrow a book. If the book is available, change its status to 'borrowed'.
        if self.status == 'available':
            self.status = 'borrowed'
            return True
        else:
            print(f"Book {self.title} is not available for borrowing.")
            return False

    def return_book(self):
        # Method to return a borrowed book. Change its status back to 'available'.
        self.status = 'available'


class User:
    def __init__(self, user_id, name):
        # Initialize a User instance with attributes such as user ID, and name, and an empty list for borrowed books.
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        # Method for a user to borrow a book. If successful, add the book's ISBN to the user's borrowed_books list.
        if book.borrow_book():
            self.borrowed_books.append(book.isbn)
            return True
        else:
            return False

    def return_book(self, book):
        # Method for a user to return a borrowed book. Remove the book's ISBN from the user's borrowed_books list.
        book.return_book()
        if book.isbn in self.borrowed_books:
            self.borrowed_books.remove(book.isbn)
    
    def get_borrowed_books(self):
        # Method to get the list of books currently borrowed by the user.
        return self.borrowed_books


class Library:
    def __init__(self):
        # Initialize a Library instance with empty dictionaries to store books and users.
        self.books = {}
        self.users = {}

    def add_book(self, book):
        # Method to add a book to the library by ISBN.
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        # Method to remove a book from the library by ISBN.
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed from the library.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

    def register_user(self, user):
        # Method to register a user in the library by user ID.
        self.users[user.user_id] = user

    def borrow_book(self, user_id, isbn):
        # Method for a user to borrow a book from the library.
        if user_id in self.users and isbn in self.books:
            user = self.users[user_id]
            book = self.books[isbn]
            if user.borrow_book(book):
                print(f"User {user.name} borrowed book {book.title}.")
            else:
                print(f"User {user.name} couldn't borrow book {book.title}.")
        else:
            print("User or book not found.")

    def return_book(self, user_id, isbn):
        # Method for a user to return a borrowed book to the library.
        if user_id in self.users and isbn in self.books:
            user = self.users[user_id]
            book = self.books[isbn]
            user.return_book(book)
            print(f"User {user.name} returned book {book.title}.")
        else:
            print("User or book not found.")

    def search_books(self, keyword):
        # Method to search for books in the library by keyword (in title or author).
        result = []
        for isbn, book in self.books.items():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                result.append(book)
        return result

    def list_available_books(self):
        # Method to list all available books in the library.
        available_books = [book for book in self.books.values() if book.status == 'available']
        return available_books


# Test the system
library = Library()

# Add books to the library
book1 = Book('001', 'Book 1', 'Author 1', 2000)
book2 = Book('002', 'Book 2', 'Author 2', 2005)
book3 = Book('003', 'Book 3', 'Author 1', 2010)
book4 = Book('004', 'Book 4', 'Author 3', 2015)
book5 = Book('005', 'Book 5', 'Author 2', 2020)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

# Register users
user1 = User('101', 'User 1')
user2 = User('102', 'User 2')

library.register_user(user1)
library.register_user(user2)

# Borrow and return books
library.borrow_book('101', '001')
library.borrow_book('102', '002')
library.borrow_book('102', '003')

library.return_book('101', '001')
library.return_book('102', '002')

# List available books
print("Available Books:")
for book in library.list_available_books():
    print(f"{book.title} by {book.author}")

# Search for books by author
print("\nBooks by Author 2:")
author2_books = library.search_books('Author 2')
for book in author2_books:
    print(f"{book.title} by {book.author}")

# Print user details
print("\nUser 2's Borrowed Books:")
user2_borrowed_books = library.users['102'].get_borrowed_books()
for isbn in user2_borrowed_books:
    book = library.books[isbn]
    print(f"{book.title} by {book.author}")


from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add book to library
    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book '{book.get_title()}' added to the library.")

    # Register member
    def register_member(self, member: Member):
        self.members.append(member)
        print(f"Member '{member.get_name()}' registered successfully.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            book.display_info()

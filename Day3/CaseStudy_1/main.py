from book import Book
from member import Member
from library import Library

def main():
    # Create library
    library = Library()

    # Add books
    book1 = Book("Python Basics", "Alice", "ISBN001")
    book2 = Book("Learning OOP", "Bob", "ISBN002")
    book3 = Book("Data Science 101", "Charlie", "ISBN003")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Register members
    member1 = Member("Alice", "M001")
    member2 = Member("John", "M002")
    library.register_member(member1)
    library.register_member(member2)

    # Display books before borrowing
    library.display_books()

    # Borrowing books
    member1.borrow_book(book1)  # Success
    member1.borrow_book(book2)  # Success
    member1.borrow_book(book3)  # Success
    member1.borrow_book(book2)  # Should fail (limit reached)
    member2.borrow_book(book1)  # Should fail (already borrowed)

    # Display books after borrowing
    library.display_books()

    # Returning a book
    member1.return_book(book1)
    member2.borrow_book(book1)  # Now should succeed

    # Final display
    library.display_books()

if __name__ == "__main__":
    main()

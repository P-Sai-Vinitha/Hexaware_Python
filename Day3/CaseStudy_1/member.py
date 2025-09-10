from book import Book

class Member:
    MAX_BORROW_LIMIT = 3

    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []  # private list

    # Getters
    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    # Borrow book method
    def borrow_book(self, book: Book):
        if len(self.__borrowed_books) >= Member.MAX_BORROW_LIMIT:
            print(f"{self.__name} cannot borrow more than {Member.MAX_BORROW_LIMIT} books.")
            return

        if book.is_available():
            book.set_availability(False)
            self.__borrowed_books.append(book)
            print(f"Member {self.__name} borrowed '{book.get_title()}'.")
        else:
            print(f"Book '{book.get_title()}' is currently not available.")

    # Return book method
    def return_book(self, book: Book):
        if book in self.__borrowed_books:
            book.set_availability(True)
            self.__borrowed_books.remove(book)
            print(f"Member {self.__name} returned '{book.get_title()}'.")
        else:
            print(f"{self.__name} has not borrowed '{book.get_title()}'.")
